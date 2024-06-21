import serial
import cv2
import numpy as np
import os

def adjust_brightness(image, brightness, factor=2.0):
    brightness = np.clip(brightness * factor, 0, 255)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * (brightness / 255.0), 0, 255)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def apply_color_filter(image, color, alpha=0.7):
    overlay = np.full(image.shape, color, dtype='uint8')
    return cv2.addWeighted(image, 1 - alpha, overlay, alpha, 0)

# Open serial port
ser = serial.Serial('COM3', 9600, timeout=1)

# video path
video_paths = [
    'video1.mp4',
    'video2.mp4',
    'video3.mp4'
]


for path in video_paths:
    if not os.path.exists(path):
        print(f"Video file not found: {path}")

# Video capture setup
videos = [cv2.VideoCapture(path) for path in video_paths]

# Check if the video can open
for i, video in enumerate(videos):
    if not video.isOpened():
        print(f"Failed to open video {i + 1}")

# Initial brightness and color filter values
brightness = [1.0, 1.0, 1.0]
color_filter = np.array([0, 0, 0])

while True:
    line = ser.readline().decode('utf-8', errors='ignore').strip()  
    if line:
        data = line.split(',')
        if data[0] == "VEML7700":
            channel = int(data[1])
            lux = float(data[2])
            brightness[channel] = lux/10 # Normalize lux value for brightness
            print("Brightness:", brightness)
        elif data[0] == "APDS9960":
            r = int(data[2])
            g = int(data[3])
            b = int(data[4])
            color_filter = np.array([r, g, b])
            print("Color Filter:", color_filter)

    for i, video in enumerate(videos):
        if not video.isOpened():
            print(f"Video {i + 1} is not opened. Skipping.")
            continue

        ret, frame = video.read()
        if not ret:
            print(f"Failed to read frame from video {i + 1}. Restarting video.")
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = video.read()
            if not ret:
                print(f"Failed to read frame again from video {i + 1}. Skipping this video.")
                continue

        if frame is not None and frame.size > 0:  
            frame = adjust_brightness(frame, brightness[i] * 255, factor=2.0)
            frame = apply_color_filter(frame, color_filter, alpha=0.7)
            cv2.imshow(f'Video {i + 1}', frame)
        else:
            print(f"Empty frame detected from video {i + 1}. Skipping this frame.")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
for video in videos:
    video.release()
cv2.destroyAllWindows()
ser.close()

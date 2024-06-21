
# Interactive Mural: Exploring Sunlight and Sensor-Based Art

<img width="445" alt="スクリーンショット 2024-06-21 17 39 42" src="https://github.com/s0umaaa/arduinoProject/assets/62178616/7d7da359-a159-490f-8d9e-dea5fdb31f3d">

### Project Overview
The project is an interactive work of art that mimics a mural that reflects the color, movement, and light of the sun, under the theme "Fusion of Nature and Science". Using real-time data from light and color sensors, this immersive, reactive artwork dynamically adjusts to changes in the environment. Arduino and iPad were used for implementation, and the outer frame (mural) was designed using a laser cutter. Please click on the Youtube link below to see the design of the artwork.

[![YouTube Video](https://img.youtube.com/vi/2enRfUNRr8E/0.jpg)](https://www.youtube.com/watch?v=2enRfUNRr8E)






### Features
- **Real-time Light Simulation:** The mural dynamically adjusts brightness and color based on real-time data from light and color sensors.
- **Immersive Experience:** The installation provides a unique, engaging experience that transforms viewers into active participants.
- **Innovative Art:** Combines technology and art to create new possibilities for artistic expression.

### Components
1. **Display Screen:** A digital canvas displaying a mural pattern that changes based on sensor input.
2. **Light Sensor:** Detects ambient brightness and adjusts the display accordingly.
3. **Color Sensor:** Captures color information from a light source and applies corresponding filters to the display.
4. **Microcontroller (Adafruit Feather ESP32 V2):** Processes sensor inputs and communicates with the display system.

### Installation
1. Clone this repository.
   ```bash
   git clone https://github.com/s0umaaa/arduinoProject.git
   ```
2. Upload the Arduino code (`project.ino`) to the Adafruit Feather ESP32 V2 microcontroller.
3. Run the Python script (`main.py`) to start the system.
   ```bash
   python main.py
   ```

### Usage
- Point a light source (e.g., smartphone flashlight) at the sensors to see the mural adjust in real-time.
- Experiment with different light conditions to explore various visual effects.

### Video Explanation
For a detailed explanation of the project, please watch our [YouTube video](https://www.youtube.com/watch?v=2enRfUNRr8E).

### Members
- Sixuan Chen
- Jiayuan Li

---

## 日本語

<img width="445" alt="スクリーンショット 2024-06-21 17 39 42" src="https://github.com/s0umaaa/arduinoProject/assets/62178616/ed78cbb9-d239-41b9-bf62-6dea1db08d26">


### プロジェクト概要
このプロジェクトは、「自然と科学の融合」というテーマで、太陽の色、動き、光を反映させる壁画を模造したインタラクティブな作品です。光と色のセンサーからのリアルタイムデータを利用することで、環境の変化に応じて動的に調整される没入型の反応するアート作品です。実装にはArduinoとiPadを使用し、外枠（壁画）をレーザーカッターを使用してデザインしました。作品のデザインは以下のYoutubeリンクからご覧下さい。

[![YouTube Video](https://img.youtube.com/vi/2enRfUNRr8E/0.jpg)](https://www.youtube.com/watch?v=2enRfUNRr8E)



### 特徴
- **リアルタイム光シミュレーション:** 光と色のセンサーからのリアルタイムデータに基づいて、壁画の明るさと色が動的に調整されます。
- **没入体験:** インスタレーションはユニークで魅力的な体験を提供し、視聴者を積極的な参加者に変えます。
- **革新的アート:** 技術とアートを融合させ、新しい芸術表現の可能性を創造します。

### コンポーネント
1. **ディスプレイ画面:** センサー入力に基づいてパターンが変化するデジタルキャンバス。
2. **光センサー:** 周囲の明るさを検出し、ディスプレイを調整します。
3. **色センサー:** 光源からの色情報をキャプチャし、対応するフィルターをディスプレイに適用します。
4. **マイクロコントローラー (Adafruit Feather ESP32 V2):** センサー入力を処理し、ディスプレイシステムと通信します。

### インストール
1. このリポジトリをクローンします。
   ```bash
   git clone https://github.com/s0umaaa/arduinoProject.git
   ```
2. Arduinoコード（`project.ino`）をAdafruit Feather ESP32 V2マイクロコントローラーにアップロードします。
3. Pythonスクリプト（`main.py`）を実行してシステムを起動します。
   ```bash
   python main.py
   ```

### 使用方法
- 光源（例：スマートフォンのフラッシュライト）をセンサーに向けると、壁画がリアルタイムで調整される様子を見ることができます。
- 異なる光条件を試して、さまざまな視覚効果を探求してください。

### 説明動画
プロジェクトの詳細な説明については、[YouTube動画](https://www.youtube.com/watch?v=2enRfUNRr8E)をご覧ください。

### チームメンバー
- Sixuan Chen
- Jiayuan Li

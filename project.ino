#include <Wire.h>
#include <Adafruit_VEML7700.h>
#include <Arduino_APDS9960.h>

Adafruit_VEML7700 veml = Adafruit_VEML7700();

void setup()
{
    Wire.begin();
    Serial.begin(9600);
    while (!Serial)
        ; // Wait for Serial Monitor to open
    Serial.println("\nI2C Scanner with TCA9548A");

    // Initialize sensors on different channels
    for (uint8_t i = 0; i < 3; i++)
    {
        TCA9548A(i);
        if (!veml.begin())
        {
            Serial.print("Failed to initialize VEML7700 sensor on channel ");
            Serial.println(i);
        }
        else
        {
            Serial.print("VEML7700 sensor initialized on channel ");
            Serial.println(i);
        }

        if (i < 2)
        {
            if (!APDS.begin())
            {
                Serial.print("Error initializing APDS-9960 sensor on channel ");
                Serial.println(i);
            }
        }
    }
}

void loop()
{
    // Read VEML7700 sensors
    for (uint8_t i = 0; i < 3; i++)
    {
        TCA9548A(i);
        readVEMLSensor(i);
        if (i < 2)
        {
            readAPDSSensor(i);
        }
    }

    // delay(5000); // Wait 5 seconds before the next loop
}

// Function to select the I2C bus on TCA9548A
void TCA9548A(uint8_t bus)
{
    Wire.beginTransmission(0x70); // TCA9548A address
    Wire.write(1 << bus);         // Send byte to select bus
    Wire.endTransmission();
    Serial.print("Bus selected: ");
    Serial.println(bus);
}

// Function to read VEML7700 sensor on the selected I2C bus
void readVEMLSensor(uint8_t channel)
{
    float lux = veml.readLux();
    float white = veml.readWhite();
    float als = veml.readALS();

    Serial.print("VEML7700,");
    Serial.print(channel);
    Serial.print(",");
    Serial.print(lux);
    Serial.print(",");
    Serial.print(white);
    Serial.print(",");
    Serial.print(als);
    Serial.println();
}

// Function to read APDS-9960 sensor on the selected I2C bus
void readAPDSSensor(uint8_t channel)
{
    while (!APDS.colorAvailable())
    {
        delay(5);
    }

    int r, g, b;
    APDS.readColor(r, g, b);

    Serial.print("APDS9960,");
    Serial.print(channel);
    Serial.print(",");
    Serial.print(r);
    Serial.print(",");
    Serial.print(g);
    Serial.print(",");
    Serial.print(b);
    Serial.println();
}

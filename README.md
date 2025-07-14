# OIBSIP_Python_Task4 - GUI Weather App (Open-Meteo)

## 🌦️ Objective
Build a user-friendly GUI weather application that shows current temperature, wind speed, and direction for any city using the **Open-Meteo API**.

## 🛠️ Steps Performed
- Used Open-Meteo API to fetch geolocation and weather data
- Designed a modern dark-themed GUI using `customtkinter`
- Allowed users to input city name to fetch weather
- Enabled unit switching between °C/°F and km/h/mph
- Displayed weather conditions with emoji-based UI

## 🧰 Tools & Libraries Used
- Python
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for GUI
- `requests` for HTTP API access
- Open-Meteo API for free weather data

## ✅ Features
- Input city name to fetch weather
- Display:
  - Temperature (°C or °F)
  - Wind Speed (km/h or mph)
  - Wind Direction (°)
- Switch between Celsius and Fahrenheit with one click
- Clean and responsive dark-themed interface

## 🔎 How to Run
1. Install the required libraries:  
   ```bash
   pip install customtkinter requests
   ```

2. Run the script:  
   ```bash
   python Weather_App.py
   ```

3. Enter a city name and click **"Get Weather"**

4. Use **"Switch Units"** to toggle between °C and °F

## 📂 File Structure
```
Weather_App.py           # Main Python Script
README.md                # Documentation
requirements.txt         # Library list
```

## 🌍 API Reference
- Open-Meteo Geocoding API: https://open-meteo.com/en/docs/geocoding-api
- Open-Meteo Weather API: https://open-meteo.com/en/docs

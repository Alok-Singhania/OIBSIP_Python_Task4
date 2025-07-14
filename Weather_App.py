import customtkinter as ctk
import requests

# Custom dark grey background
DARK_GREY = "#2e2e2e"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Weather App - Open-Meteo")
        self.geometry("500x300")
        self.configure(fg_color=DARK_GREY)  # Set window background

        self.units = "celsius"

        self.city_entry = ctk.CTkEntry(self, placeholder_text="Enter city name", width=300, fg_color="#3a3a3a", text_color="white")
        self.city_entry.pack(pady=20)

        # --- White border frame for "Get Weather" button ---
        self.search_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=8)
        self.search_frame.pack(pady=5)

        self.search_button = ctk.CTkButton(
        self.search_frame,
        text="Get Weather",
        command=self.get_weather,
        fg_color="#4a4a4a",
        hover_color="#5a5a5a",
        corner_radius=8,
        width=140
        )
        self.search_button.pack(padx=2, pady=2)

        # --- White border frame for "Switch Units" button ---
        self.unit_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=8)
        self.unit_frame.pack(pady=5)

        self.unit_button = ctk.CTkButton(
        self.unit_frame,
        text="Switch to °F",
        command=self.toggle_units,
        fg_color="#4a4a4a",
        hover_color="#5a5a5a",
        corner_radius=8,
        width=140
        )
        self.unit_button.pack(padx=2, pady=2)

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(size=18),
            wraplength=400,
            justify="left",
            text_color="white"
        )
        self.result_label.pack(pady=10)

    def toggle_units(self):
        self.units = "fahrenheit" if self.units == "celsius" else "celsius"
        self.unit_button.configure(text="Switch to °C" if self.units == "fahrenheit" else "Switch to °F")
        self.get_weather()

    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            self.result_label.configure(text="Please enter a city name.")
            return

        # Step 1: Get coordinates
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_res = requests.get(geo_url).json()
        if "results" not in geo_res:
            self.result_label.configure(text="City not found.")
            return

        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]

        # Step 2: Get weather
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
            f"&current_weather=true&temperature_unit={'fahrenheit' if self.units == 'fahrenheit' else 'celsius'}"
            f"&windspeed_unit={'mph' if self.units == 'fahrenheit' else 'kmh'}"
        )
        weather_res = requests.get(weather_url).json()

        if "current_weather" not in weather_res:
            self.result_label.configure(text="Weather data not available.")
            return

        weather = weather_res["current_weather"]
        unit_symbol = "°F" if self.units == "fahrenheit" else "°C"
        wind_unit = "mph" if self.units == "fahrenheit" else "km/h"

        info = (
            f"📍 {city.title()}
"
            f"🌡️ Temperature: {weather['temperature']}{unit_symbol}
"
            f"🌬️ Wind Speed: {weather['windspeed']} {wind_unit}
"
            f"🧭 Wind Direction: {weather['winddirection']}°"
        )
        self.result_label.configure(text=info)

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()

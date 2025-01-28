#Weather Dashboard API application

import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API_KEY is missing in the .env file.")
    exit()

def fetch_weather(city, units="metric"):
    """Fetch weather data from OpenWeatherMap API."""
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": units}
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def format_time(timestamp):
    """Convert a Unix timestamp to a human-readable time."""
    return datetime.fromtimestamp(timestamp).strftime("%I:%M %p")

def log_weather(city, temp, description):
    """Log weather data to a file."""
    with open("weather_log.txt", "a") as file:
        file.write(f"{datetime.now()}: {city} - {temp}° - {description}\n")

def main():
    while True:
        # Get user input for city
        city = input("\nEnter a city name (or type 'exit' to quit): ").strip()
        
        # Validate the input
        if not city:
            print("Error: City name cannot be empty. Please try again.")
            continue  # Ask again
        
        if city.lower() == "exit":
            print("Goodbye!")
            break

        # Get user input for units
        units = input("Choose temperature unit (metric for °C, imperial for °F): ").lower()
        if units not in ["metric", "imperial"]:
            print("Invalid choice. Defaulting to metric (°C).")
            units = "metric"

        # Fetch weather data
        weather_data = fetch_weather(city, units)

        if weather_data:
            # Extract weather details
            temp = weather_data["main"]["temp"]
            feels_like = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["weather"][0]["description"]
            wind_speed = weather_data["wind"]["speed"]
            country = weather_data["sys"]["country"]
            sunrise = format_time(weather_data["sys"]["sunrise"])
            sunset = format_time(weather_data["sys"]["sunset"])

            # Display the weather details
            print(f"\nWeather in {city.capitalize()}, {country}:")
            print(f"  Temperature: {temp}°")
            print(f"  Feels Like: {feels_like}°")
            print(f"  Humidity: {humidity}%")
            print(f"  Description: {description.capitalize()}")
            print(f"  Wind Speed: {wind_speed} m/s")
            print(f"  Sunrise: {sunrise}")
            print(f"  Sunset: {sunset}")

            # Log the weather data
            log_weather(city, temp, description)
        else:
            print("Error: City not found or API error occurred.")

if __name__ == "__main__":
    main()

# Weather Dashboard API application

import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the .env file
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API_KEY not found in .env file.")
    exit()

# Ask for a city name
city = input("Enter a city name: ")

# OpenWeatherMap API URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # Use "imperial" for Fahrenheit
}

# Fetch the weather data
response = requests.get(BASE_URL, params=params)

# Process the API response
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    # Print the weather details
    print(f"\nWeather in {city.capitalize()}:")
    print(f"  Temperature: {temp}°C")
    print(f"  Feels Like: {feels_like}°C")
    print(f"  Humidity: {humidity}%")
    print(f"  Description: {description.capitalize()}")
    print(f"  Wind Speed: {wind_speed} m/s")
else:
    print("Error: City not found or API error occurred.")



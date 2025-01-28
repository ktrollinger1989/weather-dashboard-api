# weather-dashboard-api
Weather dashboard API

1. Setting Up GitHub
What We Did:
1.	Created a GitHub Repository:
o	We went to GitHub and created a new repository called weather-dashboard-api.
o	During creation, we:
	Gave the repository a name.
	Checked the box to include a README.md file.
2.	Copied the Repository URL:
o	After creating the repository, we clicked the green Code button and copied the HTTPS link for the repository:
plaintext
CopyEdit
https://github.com/<your-username>/weather-dashboard-api.git
________________________________________
2. Setting Up Google Colab
What We Did:
1.	Opened Google Colab:
o	Accessed Google Colab and created a new notebook.
2.	Cloned the GitHub Repository:
o	To link the Colab environment with the GitHub repository, we used the !git clone command:
python
CopyEdit
!git clone https://github.com/<your-username>/weather-dashboard-api.git
o	This downloaded the repository into Colab.
3.	Changed to the Repository Directory:
o	To ensure all our files were saved within the GitHub repository folder, we navigated to the repository directory using:
python
CopyEdit
%cd weather-dashboard-api
4.	Checked the Repository Contents:
o	We verified the repository was cloned correctly by listing its contents:
python
CopyEdit
!ls
o	At this stage, we only saw the README.md file.
________________________________________
3. Adding the Project Files
What We Did:
1.	Created the Main Script (main.py):
o	In Colab, we created the main script for the weather dashboard using the %%writefile magic command:
python
CopyEdit
%%writefile main.py
# Your weather dashboard code here
o	This created a main.py file in the repository directory.
2.	Created the .env File:
o	To store the API key securely, we created a .env file:
python
CopyEdit
%%writefile .env
API_KEY=your_actual_api_key_here
o	This file was added to the repository directory but excluded from GitHub using a .gitignore file.
3.	Installed Dependencies:
o	We installed the required libraries (requests and python-dotenv) using:
python
CopyEdit
!pip install requests python-dotenv
________________________________________
4. Testing the Script
What We Did:
1.	Ran the Script:
o	We executed the main.py script in Colab to ensure it worked:
python
CopyEdit
!python main.py
2.	Troubleshooted Issues:
o	Debugged errors like missing API keys, incorrect city names, or network issues.
o	Tested with valid and invalid inputs to confirm proper error handling.
________________________________________
5. Saving Changes Back to GitHub
What We Did:
1.	Configured Git in Colab:
o	To enable commits, we set up Git with your username and email:
bash
CopyEdit
!git config --global user.name "Your Name"
!git config --global user.email "your-email@example.com"
2.	Added a .gitignore File:
o	To prevent the .env file from being uploaded, we created a .gitignore file:
python
CopyEdit
%%writefile .gitignore
.env
3.	Staged and Committed Changes:
o	We staged all the files:
bash
CopyEdit
!git add .
o	Committed the changes:
bash
CopyEdit
!git commit -m "Initial commit with main.py and .env setup"
4.	Pushed to GitHub:
o	We pushed the changes to the repository:
bash
CopyEdit
!git push origin main
5.	Note: We used a Personal Access Token (PAT) instead of a password for authentication.
________________________________________
6. Verifying Changes on GitHub
What We Did:
1.	Checked the repository on GitHub to confirm the main.py, .gitignore, and any other files were uploaded successfully.
2.	Verified that the .env file was excluded as intended.
________________________________________
Summary of the Environment Setup
1.	Created a GitHub repository to manage project files.
2.	Used Google Colab as the development environment.
3.	Cloned the repository into Colab and worked within the repository directory.
4.	Created and tested project files (main.py, .env).
5.	Configured Git in Colab to save and push changes to GitHub.

#Main.py Version 1:

1. Import Libraries:

import requests
from dotenv import load_dotenv
import os 
**requests is used to send HTTP requests to the OpenWeatherMap API. dotenv is used to allow the secure loading of sensitive data, like the API key, from a .env file. os is used to access the environment variables, like the API key**

2. Load Environment Variables:

# Load environment variables from the .env file
load_dotenv()
**this loads all the key-value pairs from the .env file into the environment so that they can be accessed in the script**

3. Retrieve the API Key:

# Get the API key from the .env file
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API_KEY not found in .env file.")
    exit()
**this does exactly what it says, it retrieves the API_KEY from the .env file using os.getenv() function. It checks if the key exists, and if it doesn't exist, it will let you know with the error message**

4. User Input for City Name:

# Ask for a city name
city = input("Enter a city name: ")
**this simply prompts the user to enter the name of a city they want the weather data for**

5. Define API URL and Parameters:

# OpenWeatherMap API URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # Use "imperial" for Fahrenheit
}
**BASE_URL specifies the endpoint for the OpenWeatherMAP API, or in other words, the program sends a request to get the weather information like it's visiting a web address to sk for weather data from OpenWeatherMap. params defines the query parameters, which includes the city name, or "q" = city name, "appid" = API key, and "units" = metric for Celsius or imperial for Fahrenheit**

6. Fetch Weather Data:

# Fetch the weather data
response = requests.get(BASE_URL, params=params)
**this sends a "GET" request to the API using the URL and parameters in the OpenWeatherMap API URL section of the code. It also stores the server's response in the "response" object, which holds everything the server sends back, in this case it is the weather data or error messages**

7. Process the API Response: 

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
**this checks if the API call was successful, which is status code 200. it converts the response to JSON format and extracts weather details, like temp, feel like, humidity, etc**

8. Print Weather Details

    # Print the weather details
    print(f"\nWeather in {city.capitalize()}:")
    print(f"  Temperature: {temp}°C")
    print(f"  Feels Like: {feels_like}°C")
    print(f"  Humidity: {humidity}%")
    print(f"  Description: {description.capitalize()}")
    print(f"  Wind Speed: {wind_speed} m/s")
**this part of the script simply prints the extracted weather details from part 7 in a clean, easy to read format**

9. Handle API Errors:

else:
    print("Error: City not found or API error occurred.")
**Lastly, we have a function that prints an error statement if the API call is not successful**

IN CONCLUSION:

This script loads the API key securely, prompts the user for a city name, makes an API request to fetch the weather data, extracts and displays key weather information like temperature, humidity, wind speed, etc., and handles errors if the city name is invalid or the API call fails.


#Main.py Version 2:

1. Created Log File:
def log_weather(city, temp, description):
    """Log weather data to a file."""
    print(f"Logging weather data for {city}...")
    with open("weather_log.txt", "a") as file:
        file.write(f"{datetime.now()}: {city} - {temp}° - {description}\n")
    print(f"Weather data for {city} logged successfully.")

2. Added Debugging Print Statements for:

A) Loading the .env File: print("Loading .env file...") **which indicates that the script is trying to load the .env file containing the API key**

B) API Key Validation: if not API_KEY:
    print("Error: API_KEY is missing in the .env file.")
    exit()
else:
    print("API key loaded successfully!") **which confirms whether the API key has been loaded successfully or not**

3. Fetching Weather Data: 

A) print(f"Fetching weather data for city: {city} with units: {units}...")
print("API request sent. Waiting for response...") **which prints the city name and temperature unit being used for the API call. you can use metric for Celsius or imperial for Fahrenheit. This also shows when the API request is sent**

B) Confirmation of Successful API Call: if response.status_code == 200:
    print("API response received successfully!")
else:
    print(f"Error: API responded with status code {response.status_code}") **this confirms whether the API call was successful or if an error occurred**

4. Formatting Timestamps: 

(print(f"Formatting timestamp: {timestamp}")) **this shows that the weather data from OpenWeatherMap, which is in Unix format which is basically a long number showing seconds since January 1, 1970, is being converted into a readable time using Python's datetime module, so it's easily understood***

5. Logging Weather Data: 

print(f"Logging weather data for {city}...")
print(f"Weather data for {city} logged successfully.") **This indicate when the script is writing weather data to the weather_log.txt file, and then confirms when it has been logged**

6. Script Status: 

A) print("Starting the Weather Dashboard script...") **simply shows that the script is starting its execution**

B) print("Starting weather fetch...")
print("Finished fetching weather data.") **indicates the start and end of the weather-fetching process**

C) print("Processing weather data...") **confirms the script is processing the weather data after receiving it from the API

7. Input Validation: 

if not city:
    print("Error: City name cannot be empty. Please try again.") **this displays and error message if the user enters an empty city name**

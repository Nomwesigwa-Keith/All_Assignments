#create an account from https://openweathermap.org/
#use API key from https://home.openweathermap.org/users/sign_up
#Save the API key in a file named 'apikey.py'

import requests
import pandas as pd

#set API key
API_KEY = 'f14efa6b042dc3c22ce853e17cce0bb1'



# Latitude and longitude for Kampala, Uganda
lat = 0.347596
lon = 32.582520

# Use the free endpoint for OpenWeatherMap
url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"

#Make GET requests
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # Convert the JSON data to a DataFrame
    df = pd.DataFrame(data['list'])
    print(df.head())
else:
    print(f"Error: {response.status_code}")
    print(response.text)



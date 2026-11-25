import requests
import json

API_KEY = "9034b95ba254606a7152acda7d737b7e"


while True:
        city = input("Enter your city: ").strip()
        if city.lower()=='q':
             print("Goodbye")
             break
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
        }
        response = requests.get(url, params=params)
        data = response.json()


        if response.status_code==200:
            temp = data.get("main", {}).get("temp")
            humid = data.get("main", {}).get("humidity")
            weather = data.get("weather", [{}])[0].get("description")

            print("=====================")
            print(f" Weather in {city.title()}")
            print("=====================")
            print(f"Temperature: {temp}°C")
            print(f"Weather: {weather}")
            print(f"Humidity: {humid}%")

        else:
            print("Error:", response.status_code)
            print("Message:", data.get("message", "Something went wrong"))

import requests
import json
import argparse


def fetch_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Use GitHub Copilot suggestion for error handling
    return response.json()


def display_weather(weather_data):
    weather = weather_data['weather'][0]
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"Weather: {weather['main']} ({weather['description']})")  # Use GitHub Copilot suggestion for data parsing
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")


def main():
    parser = argparse.ArgumentParser(description="Get the current weather forecast of a city.")
    parser.add_argument("city", type=str, help="Name of the city")
    args = parser.parse_args()

    api_key = 'fe7e5d806c1bf4de9c3df8d49191597d'
    try:
        weather_data = fetch_weather(api_key, args.city)
        display_weather(weather_data)
    except requests.exceptions.HTTPError as e:
        print(f"An HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
 

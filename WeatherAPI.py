import requests


class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_for_city(self, city_name):
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(api_url)
            data = response.json()
            # in the section below codes are treated differently because in the response 404 code is a string and 401 code is a number
            if data["cod"] == '404':
                print("No such city")
                return None
            if data["cod"] == 401:
                print("Invalid API key")
                return None
            return response.json()
        except requests.RequestException as e:
            print(f"Error: {e}")
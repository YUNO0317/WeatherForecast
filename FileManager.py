class FileManager:

    @staticmethod
    def save_report_to_file(content, city_name):
        with open(f"{city_name}_weather_forecast.txt", "w", encoding="cp1251") as w_file:
            w_file.write(content)
            print(f"{city_name}_weather_forecast.txt has been created")

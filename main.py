from WeatherAPI import WeatherAPI
from WeatherReport import WeatherReport
from FileManager import FileManager


def main():
    api_key = 'your_api_key_here' #Please enter your API key here
    weather_api = WeatherAPI(api_key)
    while True:
        city = input("Please enter a City name or type 'Q' to quit: ")
        if city.upper() == "Q":
            print("Quitting the program")
            break
        weather = weather_api.get_weather_for_city(city)
        if weather is None:
            continue
        report_format = input("Please select [S]hort or [F]ull report format: ")
        weather_report = ""
        while report_format.upper() not in ["S", "F"]:
            report_format = input('Incorrect option is provided. Please set [S]hort or [F]ull report format:')
        if report_format.upper() == "S":
            weather_report = WeatherReport.generate_short_report(weather)
        else:
            weather_report = WeatherReport.generate_full_report(weather)
        print(weather_report)
        save_to_file = input("Do you want to save the report to file? [Y]es/[N]o: ")
        while save_to_file.upper() not in ["Y", "N"]:
            save_to_file = input("Operation isn't supported. Please set [Y]es/[N]o:")
        if save_to_file.upper() == "Y":
            FileManager.save_report_to_file(weather_report, city)


if __name__ == "__main__":
    main()

class WeatherReport:

    @staticmethod
    def generate_short_report(data):
        report = f'''City: {data['name']}
    Temperature: {data['main']['temp']}°C
    {data['weather'][0]['main']}, {data['weather'][0]['description']}
    '''
        return report

    @staticmethod
    def generate_full_report(data):
        short_report = WeatherReport.generate_short_report(data)
        report = f'''{short_report}
    Pressure: {data['main']['pressure']} hPa
    Humidity: {data['main']['humidity']} %
    Highest temperature: {data['main']['temp_max']} °C
    Lowers temperature: {data['main']['temp_min']} °C
    Wind speed: {data['wind']['speed']} m/s
    '''
        return report

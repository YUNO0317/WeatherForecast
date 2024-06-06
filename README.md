# Weather Report Application
## Description
Using a weather API, this console-based Python application brings weather information for a specified city. The user can choose between a short or full weather report format and has the option to save the weather report to a file.
## Features
- Gives current weather information for any city.
- Choose between a short or full weather report format.
- Option to save the weather report to a file.
- User-friendly input prompts and error handling.
## Source API
[Openweathermap](https://openweathermap.org/api) 
## Requirements
- Python 3.x
- An _API key_ from a weather service provider [Openweathermap](https://openweathermap.org/api).
- _Requests_ library 

### Setup
1. **_Requests_ library**
- Make sure you have the `requests` library installed. If not, install it using:
```commandline
pip install requests
```
- Use ``import requests`` in the WeatherApi.py
2. **Get an API Key:**
- Obtain an API key from the [Current Weather Data](https://openweathermap.org/current)
>! Please note you need to Sign in to receive the API Key.
## Usage

1. **Run the Application:**

    ```bash
    python main.py
    ```

2. **Follow the Prompts:**
    - Enter the city name when prompted.
    - Choose the report format: `[S]hort` or `[F]ull`.
    - View the weather report in the console.
    - Optionally save the report to a file.
    - Press key `Q` to exit the program or type another city to continue.

## Code Explanation

### Main Function
The `main` function coordinates the entire workflow of the application:

1. **API Key Setup:**
    ```python
    api_key = 'your_api_key_here'
    weather_api = WeatherAPI(api_key)
    ```

2. **Main Loop:**
    - Proposes the user to enter a city name or quit the program.
    - Gets weather data for the entered city.
    - If the weather data is not available (`None`), it asks the user to enter another city.
    - Asks the user to choose the report format (short or full).
    - Generates the corresponding weather report.
    - Displays the report
    - Optionally, users can decide whether to save it to a file.

### File Structure

1. **Main.py:**
   - The main file where the program is started, the main loop.  
   - The main classes for interacting with them are imported into this file.
   - Please Run the current file to get started
2. **WeatherAPI.py:**
    - Contains the `WeatherAPI` class with methods to interact with the weather API.
3. **WeatherReport.py:**
    - Contains the `WeatherReport` class with methods to generate short and full weather reports.
4. **FileManager.py:**
    - Contains the `FileManager` class with methods to save reports to files.
## Error handling
   - In WeatherAPI.py the program check a value for the "cod" key in the received request:
      - '404' in case for incorrect City value
      - 401 in case the value of API key is incorrect
      - RequestException processes other exceptions, for example, in case of connection problems or incorrect URL.

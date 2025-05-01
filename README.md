# Weather Dashboard

A Python-based terminal application designed to provide real-time weather data using the OpenWeather API. This program is a hands-on project demonstrating dynamic functionality, while continuously being improved as part of my learning and skill enhancement journey.

## Features
- **Current Weather Data**: Fetches and displays temperature, humidity, and general weather descriptions for any city.
- **Search History Logging**: Saves previous searches for easy reference.
- **History Management**: Ability to view, filter, and remove entries from the log file.
- **Error Handling**: Detects issues like invalid city names or API errors and provides user-friendly feedback.

## Work in Progress
This project is part of my ongoing development as a programmer. I am committed to refining its features and integrating advanced tools and technologies. Planned updates include:
1. **Migrating to FastAPI**: Transitioning from `requests` to FastAPI for improved performance, scalability, and flexibility in API handling.
2. **Database Integration**: Implementing a database to store search history persistently and support complex queries.
3. **Enhanced User Interface**: Adding visualization elements like graphs for weather trends.
4. **Modular Design**: Breaking down the program into reusable modules to simplify maintenance and enable future expansion.
5. **Advanced Filters and Analytics**: Features like date-based filtering and statistical summaries of weather data.

## Requirements
- Python 3.x
- Libraries:
    - `requests` (for current functionality)
    - Additional libraries as updates are implemented (e.g., FastAPI, SQLAlchemy).

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/weather-dashboard.git
   ```
2. Run the program:
   ```bash
   python weather_dashboard.py
   ```
3. Enter a city name to get weather data, type `'history'` to view search history, `'remove'` to manage log entries, or `'exit'` to close the program.

## About the me
This project represents my personal commitment to learning and growth. By iteratively improving this app, I am honing my skills in Python, API development, and advanced programming concepts. I welcome any feedback or collaboration to further enhance this program!

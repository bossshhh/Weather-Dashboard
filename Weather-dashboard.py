import requests
import json

# Function to fetch weather data from the API
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:  # Check if the request was successful
        weather_data = json.loads(response.text)  # Parse the response

        # Extracting data from the response
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        # Create a dictionary to store the query data
        weather_info = {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "description": description
        }

        # Append the weather data to the log file
        append_to_log(weather_info)

        return weather_info
    else:
        if response.status_code == 404:  # Check if the city was not found
            print("City not found.")
            return None
        elif response.status_code == 401:  # Check if the API key is invalid
            print("Invalid API key.")
            return None
        else:  # Handle general errors
            print("Error occurred.")
            return None

# Function to append weather data to a log file
def append_to_log(weather_info):
    log_file = "weather_log.json"  # File to store weather queries
    try:
        with open(log_file, 'a') as file:  # Open the file in append mode
            file.write(json.dumps(weather_info) + "\n")  # Write JSON data as a new line
            print(f"DEBUG: Appended weather info to log file: {weather_info}")  # Debug message
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Function to view the search history
def view_log():
    log_file = "weather_log.json"  # File to store weather queries
    try:
        # Open the log file in read mode
        with open(log_file, "r") as file:
            print("\nSearch History:")
            empty = True  # Flag to check if the log file is empty
            for line in file:
                line = line.strip()
                if not line:  # Skip blank lines
                    continue
                try:
                    # Parse each line as JSON and display it
                    weather_data = json.loads(line)
                    print(f"City: {weather_data['city']}, Temperature: {weather_data['temperature']}°C, "
                          f"Humidity: {weather_data['humidity']}%, Description: {weather_data['description']}")
                    empty = False
                except json.JSONDecodeError:
                    print(f"Skipped invalid entry: {line}")
            if empty:
                print("No search history found.\n")
            print("\n")
    except FileNotFoundError:
        print("No search history found. The log file does not exist.\n")
    except Exception as e:
        print(f"Error while reading search history: {e}\n")

def remove_log():
    log_file = "weather_log.json"  # File to store weather queries
    try:
        print("Remove Options:\n1. Clear entire history\n2. Remove a specific city")
        option = input("Enter 1 to clear history or 2 to remove a specific city: ").strip()

        if option == '1':  # Clear entire history
            with open(log_file, "w") as file:  # Open in write mode to overwrite file
                pass  # Creates an empty file
            print("Search history has been cleared.\n")
        elif option == '2':  # Remove a specific city
            city_to_remove = input("Enter the city name to remove: ").lower().strip()
            with open(log_file, "r") as file: # Open in read mode to check existing entries
                lines = file.readlines()
            with open(log_file, "w") as file:  # Rewrite the file without the specified city
                found = False
                for line in lines:
                    try:
                        weather_data = json.loads(line.strip())
                        if weather_data['city'].lower() != city_to_remove:
                            file.write(json.dumps(weather_data) + "\n")
                        else:
                            found = True
                    except json.JSONDecodeError:
                        file.write(line)  # Preserve invalid lines (optional)
                if found:
                    print(f"Removed entries for city: {city_to_remove}\n")
                else:
                    print(f"No entries found for city: {city_to_remove}\n")
        else:
            print("Invalid option selected. Please try again.\n")
    except FileNotFoundError:
        print("No search history found. The log file does not exist.\n")
    except Exception as e:
        print(f"Error while managing search history: {e}\n")

# Main weather dashboard function
def weather_dashboard():
    api_key = "1e19f423cd89d66fdaa96c14da53e43b"  # Your OpenWeatherMap API key

    while True:
        # Prompt user for city name or exit
        city = input("Enter city name, type 'history' to view search history, type 'remove' to manage log,"
                     " or type 'exit' to close program: ").lower().strip()

        if city == 'exit':  # Exit the program
            print("Exiting the program. Goodbye!")
            print(f"DEBUG: User input was '{city}'")  # Debug message
            break
        elif city == 'history':  # View search history
            view_log()
            continue
        elif city == 'remove':  # Remove specific city from history
            remove_log()
            continue  # Skip the rest of the loop and prompt for input again

        # Fetch weather data for valid city input
        weather = get_weather(city, api_key)
        if weather:
            print(f"\nCity: {weather['city']}")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Description: {weather['description']}\n")
        else:
            print("Weather data could not be retrieved.\n")

# Start the program
weather_dashboard()
""""
tmw we are adding: 
timestamps by creating a function 
adding weather forecast
adding a database to store the data


Fast API
PostgresSQL
"""

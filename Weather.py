import requests
from datetime import datetime
while True:
    # Function to get weather data from the OpenWeather API
    def get_weather(city_name, api_key):
        # URL for the OpenWeather API with the city and API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        
        # Send GET request to the API
        response = requests.get(url)
        
        # If the response was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract relevant data from the JSON response
            city = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_condition = data["weather"][0]["description"]
            
            # Display the weather data
            print(f"Weather in {city}:")
            print(f"- Temperature: {temperature}°C")
            print(f"- Humidity: {humidity}%")
            print(f"- Condition: {weather_condition.capitalize()}")
        else:
            print("City not found or there was an issue with the request. Please try again.")

    # Main function to interact with the user
    def main():
        # Input from the user for the city
        city_name = input("Enter the city name: ")
        
        # Replace with your OpenWeather API key
        api_key = "..."
        # Get your own API key from OpenWeather
        
        # Get and display the weather information
        get_weather(city_name, api_key)

    # Run the program
    if __name__ == "__main__":
        main()

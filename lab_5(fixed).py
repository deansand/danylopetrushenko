"""Module providing a function printing enum"""

import enum

class WeatherType(enum.Enum):

    """
    Type of the weather
    """
    SUNNY = "Sunny"
    CLOUDLY = "Cloudly"
    RAINY = "Rainy"
    FOGGY = "Foggy"

class Weather:

    """
    Creating class Weather
    """

    def __init__(self, day, city, country, temp, humidity, wind_speed, weather_type) -> None:
        self._day = day
        self._city = city
        self._country = country
        self._temp = temp
        self._humidity = humidity
        self._wind_speed = wind_speed
        self._weather_type = weather_type
  
"""
Initializing class Weather
"""

    def __str__(self):
        return f"{self._day} - {self._city}, {self._country}: {self._weather_type}, \
Temp: {self._temp}°C, Humidity: {self._humidity}%, Wind Speed: {self._wind_speed} km/h"

    """
    String what show us data from init
    """

class WeatherCalendar:

    """
    This is Weather calendar
    """

    def __init__(self):
        self.weather_entry = []

    """
    Creating empty list for entry weather 
    """

    def add_weather_entry(self, weather_entry):

        """This function do an append metod"""

        self.weather_entry.append(weather_entry)

    def find_max_temperature(self, day):

        """This function calculate maximum temperature"""

        maximum_temperature = None
        for entry in self.weather_entry:
            if entry.day == day:
                if maximum_temperature is None or entry.temp > maximum_temperature:
                    maximum_temperature = entry.temp
        if maximum_temperature is not None:
            return maximum_temperature
        else:
            return "Not enough data"

    def what_weather_is_in_lviv(self, humidity, weather_type):

        """Calculation humidity and weather type in Lviv"""

        if humidity > 80 and weather_type.RAINY:
            return "The typical day in Lviv"
        else:
            return "You are lucky, man"

    def sort_weather_entry(self):

        """This is sorting"""

        self.weather_entry.sort(key=lambda x: x.day)

    def display_calendar(self):

        """Calendar output"""

        for entry in self.weather_entry:
            print(entry)

weather_1 = Weather(2023-10-29, "Lviv", "Ukraine", 13, 1, 13, "Foggy")
weather_2 = Weather(2023-10-29, "Kyiv", "Ukraine", 16, 3, 3, "Sunny")
weather_3 = Weather(2023-10-29, "Berlin", "Germany", 4, 5, 32, "Rainy")

calendar = WeatherCalendar()
calendar.add_weather_entry(weather_1)
calendar.add_weather_entry(weather_2)
calendar.add_weather_entry(weather_3)


calendar.sort_weather_entry()
calendar.display_calendar()

max_temp = calendar.find_max_temperature("2023-10-29")
print(f"Максимальна температура в день '2023-10-29': {max_temp}°C")

WeatherType = WeatherType.RAINY
HUMIDITY = 85
RESULT = calendar.what_weather_is_in_lviv(HUMIDITY, WeatherType)
print(RESULT)

import json
class ObservationData(object):
    """A record of observation data for a given hour
    Attributes:
        Time: Time this weather data is for.
        Date: Date this weather is for.
        Wind Gust: Wind gust speed in MPH.
        Temperature: Temperature value in degrees celsius.
        Visibility: Visibility level.
        Wind Direction: Compass direction the wind is blowing in.
        Wind Speed: The wind speed in MPH.
        Weather Type: Type of weather.
        Pressure: The pressure in hpa.
        Pressure Tendency: The pressure in Pa/s.
        Dew Point: The Dew Point in C.
        Screen Relative Humidity: Humidity in %.
    """
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print self.data

    def get_time(self):
        return self.data['$']

    def get_date(self):
        return self.data['Dt']

    def get_wind_gust(self):
        return self.data['G']

    def get_temperature(self):
        return self.data['T']

    def get_visibility(self):
        return self.data['V']

    def get_wind_direction(self):
        return self.data['D']

    def get_wind_speed(self):
        return self.data['S']

    def get_weather_type(self):
        return self.data['W']

    def get_pressure(self):
        return self.data['P']

    def get_pressure_tendency(self):
        return self.data['Pt']

    def get_dew_point(self):
        return self.data['Dp']

    def get_humidity(self):
        return self.data['H']

import json
import urllib
from location_handler import LocationHandler


'''
Collect and handle weather observation data for the past 24 hours for a given location.
Provides the data in a list, with each list entry representing the following values
on an hourly basis.

    G (mph) Wind Gust
    T (C) Temperature
    V (m) Visibility
    D (compass) Wind Direction
    S (mph) Wind Speed
    W Weather Type
    P (hpa) Pressure
    Pt (Pa/s) Pressure Tendency
    Dp (C) Dew Point
    H (%) Screen Relative Humidity

'''

class ObservationHandler(object):

    location_handler = LocationHandler()
    data = []

    def get_weather_observation_data(self, location):
        location_id = self.location_handler.get_location_id(location)

        #do some error handling for this. Not all locations can be queried for weather observations
        location_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/" + \
        location_id[0] + "?res=hourly&key=7247916d-91ac-4de7-84e1-088c23dd8432"
        #try catch

        response = urllib.urlopen(location_url)
        json_data = json.load(response)
        record = json_data['SiteRep']['DV']

        #return 24 hour of weather observation, split into two dates 
        location_record = record['Location']['Period']

        hourly_data = []

        day_1 = location_record[0]['Rep']
        day_2 = location_record[1]['Rep']

        for hour in day_1:
            hourly_data.append(hour)

        for hour in day_2:
            hourly_data.append(hour)

        for i in range(0, len(hourly_data)):
            hourly_data[i]['$'] = int(hourly_data[i]['$'])/60
            hourly_data[i]['$'] = str(hourly_data[i]['$'])
            #Add 0 digits to maintain length
            if(len(hourly_data[i]['$']) < 2):
                hourly_data[i]['$'] = "0" + hourly_data[i]['$'] + ":00"
            else:
                hourly_data[i]['$'] = hourly_data[i]['$'] + ":00"

        global data
        data = hourly_data
        #Return the 24 hour data
        return hourly_data

    #Print the hourly data
    def print_hourly_data(self):
        for hour in data:
            print hour


    
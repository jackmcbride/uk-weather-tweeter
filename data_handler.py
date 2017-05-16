from location_handler import LocationHandler
import json
from pprint import pprint
import urllib

class DataHandler(object):

    location_handler = LocationHandler()

    #return a tuple of 24 hour weather data for a given location.
    '''
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
    def get_weather_observation_data(self, location):
        location_id = self.location_handler.get_location_id(location)

        #do some error handling for this. Not all locations can be queried for weather observations
        location_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/" + location_id[0] + "?res=hourly&key=7247916d-91ac-4de7-84e1-088c23dd8432"

        response = urllib.urlopen(location_url)
        
        data = json.load(response)

        record = data['SiteRep']['DV']

        #return 24 hour of weather observation, split into two dates 
        location_record = record['Location']['Period']

        print "Day 1: "
        pprint(location_record[0]['Rep'])

        print "Day 2: "
        pprint(location_record[1]['Rep'])

        #Return the two day's data...Push to git man
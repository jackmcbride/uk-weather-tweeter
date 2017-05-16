import json
from pprint import pprint
import urllib


#Handles locations as tweeted by users
class LocationHandler(object):
    
    #URL for finding the id of each location for returning weather data.
    location_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=7247916d-91ac-4de7-84e1-088c23dd8432"
    
    #return a list of location ids for a given city based location
    def get_location_id(self, location):
        #List of location ids for a given location
        id_list = []

        response = urllib.urlopen(self.location_url)
        data = json.load(response)

        #Navigate json file
        for key, value in data.items():
            for k, v in value.items():
                for record in v:
                    if record['name'] == location:
                        id_list.append(record['id'])

        return id_list

    #return a list of all regions.
    def get_unitary_authority_regions(self):
        #List of location ids for a given location
        region_list = []

        response = urllib.urlopen(self.location_url)
        data = json.load(response)

        #Navigate json file
        for key, value in data.items():
            for k, v in value.items():
                for record in v:
                    if 'unitaryAuthArea' in record:
                        region_list.append(record['unitaryAuthArea'])

        region_list = set(region_list)
        region_list = list(region_list)

        return region_list

            
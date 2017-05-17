import json
import urllib
from location import Location

#Handles locations as tweeted by users
class LocationParser(object):
    """Location parser for handling locations
    """
    def parse_obs_json_payload(self, location):
        """Parse list of observation location data.
        """
        sitelist_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/sitelist?key=7247916d-91ac-4de7-84e1-088c23dd8432"
        response = urllib.urlopen(sitelist_url)
        payload = json.load(response)

        payload = payload['Locations']['Location']

        #make sure this returns an error, or all the data will be returned.
        for p in payload:
            if p['name'] == location:
                payload = p

        return payload

    def parse_fc_json_payload(self, location):
        """Parse list of forecast location data.
        """

        sitelist_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=7247916d-91ac-4de7-84e1-088c23dd8432"
        response = urllib.urlopen(sitelist_url)
        payload = json.load(response)

        payload = payload['Locations']['Location']

        #make sure this returns an error, or all the data will be returned.
        for p in payload:
            if p['name'] == location:
                payload = p

        return payload

    def get_location_data_objects(self, payload):
        """Convert the JSON payload into a location object.
        Return that object.
        """
        for i in range(0, len(payload)):
            location = Location(payload)
        return location

            
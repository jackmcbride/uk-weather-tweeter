import json
import urllib
from location_parser import LocationParser
from observation_data import ObservationData

class ObservationDataParser(object):
    """Parser class for 24 hour weather observations for a given location.
    Converts JSON data from the met office datapoint API into ObservationData objects.
    """

    def parse_json_payload(self, location):
        """Parse a JSON payload of weather data.
        Format this as a payload to be converted
        into weather data objects.
        """
        location_id = location.get_id()

        location_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/" + \
        location_id + "?res=hourly&key=7247916d-91ac-4de7-84e1-088c23dd8432"

        response = urllib.urlopen(location_url)

        payload = json.load(response)
        payload = payload['SiteRep']['DV']
        payload = payload['Location']['Period']

        #add date keys
        for p in payload[0]['Rep']:
            p["Dt"] = payload[0]['value']

        for p in payload[1]['Rep']:
            p["Dt"] = payload[1]['value']

        #combined payload of all 24 hours
        payload = payload[0]['Rep'] + payload[1]['Rep']

        for p in payload:
            p["$"] = int(p['$']) / 60
            if len(str(p["$"])) < 2:
                p["$"] = "0" + str(p["$"]) + ":00"
            else:
                p["$"] = str(p["$"]) + ":00"

        return payload

    def get_weather_data_objects(self, payload):
        """Convert the JSON payload into weather data objects.
        Store them in a list, and return the list.
        """
        hourly_data = []
        for i in range(0, len(payload)):
            #Create new data object
            data = ObservationData(payload[i])
            hourly_data.append(data)
        return hourly_data

from location_parser import LocationParser
from observation_data_parser import ObservationDataParser
import sys

api_key = "7247916d-91ac-4de7-84e1-088c23dd8432"

def main():
    #Parse for either a weather observation, or a weather forecast.
    #locationparser.parse_obs_json_payload("Gravesend-Broadness")
    #locationparser.parse_fc_json_payload("Canterbury")

    location = ""

    for i in range(1, len(sys.argv)):
        location += sys.argv[i] + " "

    location = location.strip()

    print location

    data = get_observation_data(location)
    
    for d in data:
        d.print_data()

    return

def get_observation_data(location):
    """Get the weather observation data for a given location.
    """
    #Location parser for parsing JSON data for a given location into a python object
    locationparser = LocationParser()

    #Observation data parser parsing JSON data for a 24 hour weather observation of a location
    observationparser = ObservationDataParser()
    
    #get weather observation for Gravesend-Broadness
    l = locationparser.parse_obs_json_payload(location)

    lobject = locationparser.get_location_data_objects(l)

    #Check this is correct.
    #lobject.print_data()

    #Parse the observation data for that location
    payload = observationparser.parse_json_payload(lobject)

    #Parse that data into a list of python objects
    return observationparser.get_weather_data_objects(payload)

def get_forecast_data(location):
    """Get the weather forecast data for a given location.
    """
    #Forecast data parser parsing JSON data for a forecast of a location [TO WRITE]
    #forecastparser = ForecastDataParser()
    return 

main()
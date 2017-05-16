from scraper import Scraper
from location_handler import LocationHandler
from observation_handler import ObservationHandler

api_key = "7247916d-91ac-4de7-84e1-088c23dd8432"

def main():
    #Handler class for locations in the UK
    locationhandler = LocationHandler()
    #Handler class for 24Hr weather observations 
    obshandler = ObservationHandler()

    obshandler.get_weather_observation_data("Gravesend-Broadness")
    obshandler.print_hourly_data()

    return

main()
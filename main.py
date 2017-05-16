from scraper import Scraper
from location_handler import LocationHandler
from data_handler import DataHandler

api_key = "7247916d-91ac-4de7-84e1-088c23dd8432"

def main():
    locationhandler = LocationHandler()
    datahandler = DataHandler()

    datahandler.get_weather_observation_data("Gravesend-Broadness")

    return

main()
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

flight_search = FlightSearch()
data_manager = DataManager()
flights_data = data_manager.apiCall()


for flight in flights_data:
    if not flight["iataCode"]:
        flight["iataCode"] = flight_search.set_iat_code()

pprint(flights_data)        
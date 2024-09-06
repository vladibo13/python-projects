from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
import time

flight_search = FlightSearch()
data_manager = DataManager()
flights_data = data_manager.api_call()


for flight in flights_data:
    if not flight["iataCode"]:
        flight["iataCode"] = flight_search.set_iat_code(flight["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
pprint(flights_data)        
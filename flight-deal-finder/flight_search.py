import os
import requests 
from dotenv import load_dotenv

load_dotenv()

IATA_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) :
        self._api_key = os.environ["FLIGHTS_API_KEY"]
        self._api_secret = os.environ["FLIGHTS_API_SECRET"]
        self._token = self._get_new_token()

    def set_iat_code(self, city):
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {
            "keyword": city.upper(),
            "max": "2",
            "include": "AIRPORTS"
        } 
        response = requests.get(url = IATA_URL, headers=headers, params=params)
        print(response)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code
    
    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=os.environ["TOKEN_URL"], headers=header, data=body)

         # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
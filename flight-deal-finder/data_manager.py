from pprint import pprint
import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_URL=os.getenv("SHEETY_URL")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def api_call(self):
        response = requests.get(url=SHEETY_URL)
        data = response.json()
        pprint(data)
        return data["prices"]
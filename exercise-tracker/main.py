import requests 
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

SHEETY_URL=os.getenv("SHEETY_URL")
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
AUTH_HEADERS =  {
    "x-app-id": os.getenv('APP_ID'),
    "x-app-key": os.getenv('API_KEY')
}
user_input = input(" Tell Me What you did?")

params = {
    "query": user_input,
    "weight_kg": os.getenv('WEIGHT'),
    "height_cm": os.getenv('HEIGHT'),
    "age": os.getenv('AGE')
}

response = requests.post(url=NUTRITIONIX_URL, json = params, headers = AUTH_HEADERS)
exercises_list = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercises_list["exercises"]:
    exercise_input = {
      "workout": {
        "Date": today_date,
        "Time": now_time,
        "Exercise": exercise["name"],
        "Duration": exercise["duration_min"],
        "Calories": exercise["nf_calories"]
      }
    }
    workout_response = requests.post(url=SHEETY_URL, json = exercise_input)
    print(workout_response.text)
    print(exercise)

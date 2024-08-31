import requests 
from newsapi import NewsApiClient
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_NAME = os.getenv('STOCK_NAME')
COMPANY_NAME = os.getenv('COMPANY_NAME')
TWILIO_API_KEY = os.getenv('TWILIO_API_KEY')

STOCK_ENDPOINT = os.getenv('STOCK_ENDPOINT ')
NEWS_ENDPOINT = os.getenv('NEWS_ENDPOINT')

STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
TWILIO_API_KEY = os.getenv('TWILIO_API_KEY ')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# 1.
stock_response = requests.get(STOCK_ENDPOINT, stock_params)
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yestarday_data = data_list[0]
yestarday_closing_price = yestarday_data["4. close"]

#2
day_before_yestarday = data_list[1]
day_before_yestarday_closing_price = day_before_yestarday["4. close"]

#3
positive_difference = abs(float(yestarday_closing_price) - float(day_before_yestarday_closing_price))


#4
diff_percentage = (positive_difference / float(yestarday_closing_price)) * 100
print(yestarday_closing_price,day_before_yestarday_closing_price, positive_difference, diff_percentage)

#5

newsapi = NewsApiClient(api_key = NEWS_API_KEY)
all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                      language='en',
                                      sort_by='relevancy',
                                      page=1
                                      )
print(all_articles["articles"][0:3])
top_articles = all_articles["articles"][0:3]

client = Client(TWILIO_API_KEY, TWILIO_AUTH_TOKEN)

for article in top_articles:
    message = client.messages.create(
        body = article,
        from_ = os.getenv('FROM'),
        to = os.getenv('TO')
    )


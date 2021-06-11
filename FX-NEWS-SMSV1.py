# SITES USED

# RATES https://www.alphavantage.co
# NEWS https://newsapi.org
# SMS https://www.twilio.com/

import requests
from twilio.rest import Client
import datetime

VIRTUAL_TWILIO_NUMBER = #
VERIFIED_NUMBER = #

BASE_CURRENCY = "CAD"
SECOND_CURRENCY = "USD"
COMPANY_NAME = "USDCAD"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "KEY"
NEWS_API_KEY = "KEY"
TWILIO_SID = "KEY"
TWILIO_AUTH_TOKEN = "KEY"

TODAY = datetime.date.today()
YESTERDAY = datetime.timedelta(1)

stock_params = {
    "function": "FX_DAILY",
    "from_symbol": BASE_CURRENCY,
    "to_symbol": SECOND_CURRENCY,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
print(response)
data = response.json()["Time Series FX (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
print(yesterday_data)
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0.00001:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = ((difference / float(yesterday_closing_price))) * 100
diff_percent = round(diff_percent, 3)
print(diff_percent)

if abs(diff_percent) < 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "from": YESTERDAY,
        "to": TODAY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    one_articles = articles[:1]
    print(one_articles)
    
    formatted_articles = [f"{BASE_CURRENCY}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in one_articles]
    print(formatted_articles)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )

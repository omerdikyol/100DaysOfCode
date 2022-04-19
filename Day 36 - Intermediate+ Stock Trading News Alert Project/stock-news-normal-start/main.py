import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "0V0KUG3SAJPQFXLK"
NEWS_API_KEY = "903c6a1e85a646e08cd2d2d26d308cd7"
TWILIO_SID = ""
TWILIO_TOKEN = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "datatype": "json",
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

# TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_closing_price = float(data_list[1]["4. close"])
print(before_yesterday_closing_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yesterday_closing_price - before_yesterday_closing_price)
print(difference)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percentage = 100 * (difference / before_yesterday_closing_price)
print(difference_percentage)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if difference_percentage > 5:
#     print("Get News")

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if difference_percentage > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": "Tesla",
    }
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    response2 = requests.get(url=NEWS_ENDPOINT, params=news_params)
    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    news_data = response2.json()["articles"][:3]
    print(news_data)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    three_articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in news_data]
    print(three_articles)

    # TODO 9. - Send each article as a separate message via Twilio.
    # from twilio.rest import Client
    # client = Client(TWILIO_SID, TWILIO_TOKEN)
    #
    # for article in three_articles:
    #     message = client.messages.create(
    #         body=article,
    #         from="",
    #         to="MYPHONENUMBER",
    #     )

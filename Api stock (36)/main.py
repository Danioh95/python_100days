import requests
import re
import newsapi

# from newsapi import NewsApiClient



# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

regex = re.compile('2022-11-[0-1][0-9]')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
function="TIME_SERIES_DAILY_ADJUSTED"
apikey= "5SQDIOJDAKH7VQGT"

parameter = {
        "function":"TIME_SERIES_DAILY_ADJUSTED",
        "symbol":STOCK,
        "apikey":apikey
}

r = requests.get('https://www.alphavantage.co/query', params=parameter)

out = r.json()

list_open = [out["Time Series (Daily)"][x]["1. open"] for x in out["Time Series (Daily)"] if re.match(regex,x)]

list_close = [out["Time Series (Daily)"][x]["4. close"] for x in out["Time Series (Daily)"] if re.match(regex,x)]



# difference = [print(type(list_close[x])) for x in range(len(list_close))]
difference = [(abs(float(list_close[x])-float(list_open[x]))/float(list_close[x])*100) for x in range(len(list_close))
              if (abs(float(list_close[x])-float(list_open[x]))/float(list_close[x])*100) > 5]


if len(difference) > 0:
        print("attention")
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

apikey2 ="1842c2a9f2974f1e92d42be0b4c1c7ec"
# newsapi = NewsApiClient(api_key='1842c2a9f2974f1e92d42be0b4c1c7ec')
parameter2 = {
        "q":"Tesla",
        "from":"2022-11-01",
        "sortBY":"popularity",
        "apiKey":apikey2
}
r2 = requests.get('https://newsapi.org/v2/everything', params=parameter2)
out2 = r2.json()["articles"]

articles = [out2[x]["content"] for x in range(len(out2)) if x < 3]

[print(articles[x]) for x in range(len(articles))]
## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """


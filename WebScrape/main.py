from importlib.metadata import version
import requests


headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
stockSymbol = 'AAPL'
url = 'https://finance.yahoo.com/quote/'+ stockSymbol + '/key-statistics?p=' + stockSymbol
resp = requests.get(url, headers=headers, timeout=5).text
print(resp)


# my_url = 'https://finance.yahoo.com/topic/stock-market-news/'
# response = requests.get(my_url)
# print("response.ok : {} , response.status_code : {}".format(response.ok , response.status_code))
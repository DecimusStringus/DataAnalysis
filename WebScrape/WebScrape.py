import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
import requests

"""
Read the URL function
"""
def get_page(url):
    """Download a webpage and return a beautiful soup doc"""
    # add header to emulate opening via browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get(url, headers=headers, timeout=5)
    if not response.ok:
        print('Status code:', response.status_code)
        raise Exception('Failed to load page {}'.format(url))
    page_content = response.text
    doc = BeautifulSoup(page_content, 'html.parser')
    return doc

# Enter a stock symbol
company = 'MSFT'
# URL link
url_is = 'https://finance.yahoo.com/quote/' + company + '/financials?p=' + company
url_bs = 'https://finance.yahoo.com/quote/' + company +'/balance-sheet?p=' + company
url_cf = 'https://finance.yahoo.com/quote/' + company + '/cash-flow?p=' + company
doc = get_page(url_is)
"""
Data Manipulation
"""
ls = []  # Create empty list
# Find all data structure that is ‘div’ and financial row
for l in doc.find_all('div', {'class': "D(tbr) fi-row Bgc($hoverBgColor):h"}):
    ls.append(l.getText(';').split(';')) # add each element one by one to the list
#ls = [e for e in ls if e not in ('Operating Expenses', 'Non-recurring Events')]  # Exclude those columns
#new_ls = list(filter(None,ls))
Income_st = pd.DataFrame(ls[0:])
print(Income_st.head())


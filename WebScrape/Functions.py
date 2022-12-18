import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
import requests

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

def get_data_frame(report_type: str, company: str):
    """
    Returns pandas dataframe with financial report data
        Parameters:
            report_type (str):
                'is' - Income Statement
                'bs' - Balance Sheet
                'cf' - Cash Flow
            company (str): company name at yahoo finance
    """
    # URL link definition
    url_common = 'https://finance.yahoo.com/quote/'
    if report_type == 'is':
        url = url_common + company + '/financials?p=' + company
    elif report_type == 'bs':
        url = url_common + company +'/balance-sheet?p=' + company
    elif report_type == 'cf':
        url = url_common + company + '/cash-flow?p=' + company

    # Scrape data and transform to pandas dataframe

    bs4_doc = get_page(url) # read url to a bs4 doc
    # Find header and append to ls_header
    ls_header = [] # create empty list for header
    for t in bs4_doc.find_all('div', {'class': "D(tbhg)"}):
        ls_header.append(t.getText(';').split(';'))
    # Find all data structure that is ‘div’ and fi-row
    ls = []  # Create empty list
    for bs4_tag in get_page(url).find_all('div', {'class': "D(tbr) fi-row Bgc($hoverBgColor):h"}):
        ls.append(bs4_tag.getText(';').split(';')) # add each element one by one to the list
    # examples of filtering data:
    # ls = [e for e in ls if e not in ('Operating Expenses', 'Non-recurring Events')]  # Exclude those columns
    # new_ls = list(filter(None,ls))

    # Create data frame and name columns
    pd_df = pd.DataFrame(ls)
    pd_df.columns = ls_header

    return pd_df  # return pandas dataframe
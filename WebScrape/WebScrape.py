# import functions
from Functions import *

income_st = get_data_frame('is', 'MSFT')
balance_st = get_data_frame('bs', 'MSFT')
cash_flow = get_data_frame('cf', 'MSFT')
print(income_st.head())
print(balance_st.head())
print(cash_flow.head())


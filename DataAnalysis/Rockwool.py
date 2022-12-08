import pandas
import numpy
import matplotlib.pyplot as plt
import xlrd

path = "C:/Users/48885/Documents/Python Knowledge/Rockwool/"
#rockwool = pandas.read_excel(path + 'Quotes-1817.xls', header=3, index_col=0).rename(columns={'Close': 'CloseA', 'Volume': 'VolumeA', 'Close.1': 'CloseB', 'Volume.1': 'VolumeB'})
rockwool = pandas.read_excel(path + 'Quotes-1817.xls', header=None, index_col=0, skiprows=4)
rw_2022a = rockwool.loc['2022-01-01':'2022-12-31']
#rw_2022a['diffA'] = rw_2022a['Close'].shift(1) - rw_2022a['Close']
#rw_2022a['diffA'] = rw_2022a[:, ('Close', '')].shift(1) - rw_2022a[:, ('Close', '')]
#rw_2022a['ma50A'] = rw_2022a['CloseA'].rolling(50).mean()

#print(rw_2022a.head())
#print(rw_2022a.loc['2022-01-03'])

print(rockwool.head())



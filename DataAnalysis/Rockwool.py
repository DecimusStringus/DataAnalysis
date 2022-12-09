import pandas
#import numpy
import matplotlib.pyplot as plt
#import xlrd

path = "C:/Users/48885/Documents/Python Knowledge/Rockwool/"
rockwool = pandas.read_excel(path + 'Quotes-1817.xls', header=3, index_col=0).rename(columns={'Close': 'CloseA', 'Volume': 'VolumeA', 'Close.1': 'CloseB', 'Volume.1': 'VolumeB'})
#rockwool = pandas.read_excel(path + 'Quotes-1817.xls', header=None, index_col=0, skiprows=4)
rw_2022 = rockwool.loc['2022-01-01':'2022-12-31'].copy() # copy() helps to get rid of a warning message
rw_2022['DiffA'] = rw_2022['CloseA'].shift(1) - rw_2022['CloseA']
#rw_2022a['diffA'] = rw_2022a[:, ('Close', '')].shift(1) - rw_2022a[:, ('Close', '')]
rw_2022['ma50A'] = rw_2022['CloseA'].rolling(50).mean()
rw_2022['ma20A'] = rw_2022['CloseA'].rolling(20).mean()
rw_2022['ma50B'] = rw_2022['CloseB'].rolling(50).mean()
rw_2022['ma20B'] = rw_2022['CloseB'].rolling(20).mean()

plt.figure(figsize=(10, 8))

rw_2022['CloseA'].plot(label='CloseA')
rw_2022['CloseB'].plot(label='CloseB')
#rw_2022['VolumeA'].plot(label='VolumeA')
#rw_2022['ma50A'].plot(label='ma50A')
#rw_2022['ma20A'].plot(label='ma20A')
rw_2022['ma50B'].plot(label='ma50B')
rw_2022['ma20B'].plot(label='ma20B')
plt.legend()
plt.show()
#print(rw_2022.tail())
#print(rw_2022.loc['2022-01-03'])

#print(rockwool.head())



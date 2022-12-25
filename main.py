import pandas
#import numpy
import matplotlib.pyplot as plt
#import xlrd

#path = "C:/Users/48885/Documents/Python Knowledge/Rockwool/"
file_path = r"C:\Users\48885\Documents\Python Knowledge\Rockwool\Quotes-1817.xls"
#rockwool = pandas.read_excel(path + 'Quotes-1817.xls', header=3, index_col=0).rename(columns={'Close': 'CloseA', 'Volume': 'VolumeA', 'Close.1': 'CloseB', 'Volume.1': 'VolumeB'})
rockwool = pandas.read_excel(file_path, header=3, index_col=0).rename(columns={'Close': 'CloseA', 'Volume': 'VolumeA', 'Close.1': 'CloseB', 'Volume.1': 'VolumeB'})

print(rockwool['CloseA'].count())
"""
lesson 1
"""
# #import the package "Pandas" into Jupyter Notebook
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# #We import the stock data of Facebook into Jupyter Notebook. The CSV file is located in the folder called "Data" in your Workspace
# #We then name the DataFrame name as 'fb'
# #Define path
# path = "C:/Users/48885/Documents/Python Knowledge/Coursera/work/data/"
# fb = pd.read_csv(path + 'facebook.csv', index_col=0)
# ms = pd.read_csv(path + 'microsoft.csv', index_col=0)
#
# # Select subset from dataframe fb
# fb.loc['2015-01-01':'2015-12-31', 'Close'].plot()
# # Using plt.show() to show plot
# plt.show()
"""
lesson 2
"""
# print summary statistics of Facebook
# print(fb.describe())
# # select all the price information of Facebook in 2016.
# fb_2015 = fb.loc['2015-01-01':'2015-12-31']
# #Plot the stock data using plot() method
# plt.figure(figsize=(10, 8))
# fb['Close'].plot()
# plt.show()
"""
Outcomes and Variables
"""
#import numpy and pandas package
import numpy as np
import pandas as pd

# roll two dice for multiple times
die = pd.DataFrame([1, 2, 3, 4, 5, 6])
sum_of_dice = die.sample(2, replace=True).sum().loc[0]
print('Sum of dice is', sum_of_dice)
# you may get different outcomes as we now mimic the result of rolling 2 dice, but the range must be limited between 2 and 12.

# The following code mimics the roll dice game for 50 times. And the results are all stored into "Result"
# Lets try and get the results of 50 sum of faces.
trial = 50
result = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
#print the first 10 results
print(result[:10])
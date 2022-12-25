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
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# # roll two dice for multiple times
# die = pd.DataFrame([1, 2, 3, 4, 5, 6])
# sum_of_dice = die.sample(2, replace=True).sum().loc[0]
# #print('Sum of dice is', sum_of_dice)
# # you may get different outcomes as we now mimic the result of rolling 2 dice, but the range must be limited between 2 and 12.
#
# # The following code mimics the roll dice game for 50 times. And the results are all stored into "Result"
# # Lets try and get the results of 50 sum of faces.
# trial = 50
# results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
# #print the first 10 results
# #print(results[:10])
# """
# Frequency and Distribution
# """
# # This is the code for summarizing the results of sum of faces by frequency
# freq = pd.DataFrame(results)[0].value_counts()
# sort_freq = freq.sort_index()
# #print(sort_freq)
# #plot the bar chart base on the result
# sort_freq.plot(kind='bar', color='blue', figsize=(15, 8))
# #plt.show()
# """
# Relative Frequency
# """
# # Using relative frequency, we can rescale the frequency so that we can compare results from different number of trials
# relative_freq = sort_freq/trial
# relative_freq.plot(kind='bar', color='blue', figsize=(15, 8))
# #plt.show()
#
# # Let us try to increase the number of trials to 10000, and see what will happen...
# trial = 10000
# results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
# freq = pd.DataFrame(results)[0].value_counts()
# sort_freq = freq.sort_index()
# relative_freq = sort_freq/trial
# relative_freq.plot(kind='bar', color='blue', figsize=(15, 8))
#
# # We can see that with more trials, the result looks more and more stable, and this is very close to a probability distribution.
# # Try increasing the number of "trial" further (but it may take some time for Jupyter Notebook to output the result)
# """
# Expectation and Variance of a distribution
# """
# # assume that we have fair dice, which means all faces will be shown with equal probability
# # then we can say we know the 'Distribtuion' of the random variable - sum_of_dice
#
# X_distri = pd.DataFrame(index=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# X_distri['Prob'] = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
# X_distri['Prob'] = X_distri['Prob']/36
# #print(X_distri)
#
# mean = pd.Series(X_distri.index * X_distri['Prob']).sum()
# var = pd.Series(((X_distri.index - mean)**2)*X_distri['Prob']).sum()
#
# #Output the mean and variance of the distribution. Mean and variance can be used to describe a distribution
# #print(mean, var)
#
# """
# Empirical mean and variance
# """
#
# # if we calculate mean and variance of outcomes (with high enough number of trials, eg 20000)...
# trial = 20000
# results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
#
# #print the mean and variance of the 20000 trials
# results = pd.Series(results)
#print(results.mean(), results.var())

"""

Models of Stock Return

"""
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# path = "C:/Users/48885/Documents/Python Knowledge/Coursera/work/data/"
# # fb = pd.read_csv(path + 'facebook.csv', index_col=0)
# ms = pd.read_csv(path + 'microsoft.csv', index_col=0)
# #print(ms.head())
# """
# Distribution of Log return
# """
# # let play around with ms data by calculating the log daily return
# ms['LogReturn'] = np.log(ms['Close']).shift(-1) - np.log(ms['Close'])
# # Plot a histogram to show the distribution of log return of Microsoft's stock.
# # You can see it is very close to a normal distribution
# from scipy.stats import norm
# mu = ms['LogReturn'].mean()
# sigma = ms['LogReturn'].std(ddof=1)
#
# density = pd.DataFrame()
# density['x'] = np.arange(ms['LogReturn'].min()-0.01, ms['LogReturn'].max()+0.01, 0.001)
# density['pdf'] = norm.pdf(density['x'], mu, sigma)
#
# ms['LogReturn'].hist(bins=50, figsize=(15, 8))
# plt.plot(density['x'], density['pdf'], color='red')
# #plt.show()
#
# """
# Calculate the probability of the stock price will drop over a certain percentage in a day
# """
# # probability that the stock price of microsoft will drop over 5% in a day
# prob_return1 = norm.cdf(-0.05, mu, sigma)
# #print('The Probability is ', prob_return1)
#
# """
# Calculate the probability of the stock price will drop over a certain percentage in a year
# """
# # drop over 40% in 220 days
# mu220 = 220*mu
# sigma220 = (220**0.5) * sigma
# #print('The probability of dropping over 40% in 220 days is ', norm.cdf(-0.4, mu220, sigma220))
#
# """
# Calculate Value at risk (VaR)
# """
# # Value at risk(VaR)
# VaR = norm.ppf(0.05, mu, sigma)
# #print('Single day value at risk ', VaR)
#
# # Quatile
# # 5% quantile
# #print('5% quantile ', norm.ppf(0.05, mu, sigma))
# # 95% quantile
# #print('95% quantile ', norm.ppf(0.95, mu, sigma))


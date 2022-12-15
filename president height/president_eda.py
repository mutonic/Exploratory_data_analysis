# This code looks like it is performing an exploratory data analysis on the heights of US Presidents. The code reads in a CSV file containing the heights of US Presidents, then uses various methods from the pandas library to calculate and display some summary statistics about the data, such as the mean, standard deviation, minimum, and maximum height. The code also generates a histogram of the data and identifies the shortest and tallest US Presidents in history. Overall, this is a well-written and well-commented code that effectively uses the pandas library to perform an exploratory data analysis on the heights of US Presidents.

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#filter warnings
import warnings
warnings.filterwarnings('ignore')

#load data
df = pd.read_csv('president_heights.csv')
df.head()

#look for dataframe dimension
df.shape

#data summary
df['height(cm)'].describe()

print('The mean is = ', round(df['height(cm)'].mean(),2))
print('The standard deviation is = ', round(df['height(cm)'].std(), 2))
print('The minimum is = ', round(df['height(cm)'].min(),2))
print('The maximum is = ', round(df['height(cm)'].max(),2))
print('The 25th percentile = ', round(np.percentile(df['height(cm)'], 25),2))
print('The median = ', round(df['height(cm)'].median(), 2))
print('The 75th percentile = ', round(np.percentile(df['height(cm)'], 75),2))

#visualize on distribution plot
sns.distplot(df['height(cm)'], hist = True, kde = True,bins=10, label='Height distribution of USA President')
plt.title('Height distribution of USA president')
plt.xlabel('height(cm)')
plt.ylabel('Number')
plt.show()

# The shortest president
df.loc[df['height(cm)'].idxmin()][1]

#The tallest president
mask = df['height(cm)'] == 193
df.name[mask]

df['height(cm)'].value_counts()

# sort the table from the tallest president to the smallest in the US history
df.sort_values(by= 'height(cm)',ascending=False)

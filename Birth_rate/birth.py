# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Load dataset of births
data = pd.read_csv('births.csv')

# Check for missing values
data.isnull().sum()

# Summarize statistics
data.describe()

# Convert 'day' column to datetime data type
data['day'] = pd.to_datetime(data['day'], format='%d')

# Impute missing values with zeros
data['day'].fillna(0, inplace=True)

# Create 'decade' column
data['decade'] = 10 * (data['year'] // 10)

# Create pivot table to visualize total number of births by gender and decade
births_gender_decade = data.pivot_table('births', index='decade', columns='gender', aggfunc='sum')

# Plot total number of births by gender and decade
births_gender_decade.plot()
plt.ylabel('Total births per year')
plt.show()

# Filter out values outside of 5 standard deviations from the mean
mean = data['births'].mean()
std = data['births'].std()
data = data.query('(births > @mean - 5 * @std) & (births < @mean + 5 * @std)')

# Create 'day of week' column
data['day of week'] = data.index.dayofweek

# Create pivot table to visualize average number of births by day of week
births_day = data.pivot_table('births', index='day of week', columns='decade', aggfunc='mean')

# Set index labels
births_day.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

# Plot average number of births by day of week
births_day.plot()
plt.ylabel("Average Births by Day")
plt.show()

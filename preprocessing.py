# This script examines data from the Vaccine Adverse Effect Reporting System
#  and filter data that pertain to Covid vaccines.
# Source data: 2021/1/21

import pandas as pd

# Import source data in CSV format from VAERS
data = pd.read_csv('./data/VAERSData/2021VAERSData.csv')

# Explore the source data
print(data.columns)
print(data.tail(10))
print(data.describe())
print(data.shape)

# Define filter keywords:
keywords = ['pfizer',
            'covid',
            'covid19',
            'covid 19',
            'moderna',
            'Moderna']

# Generate a new column named Covid with boolean values based on the keywords.
data['Covid']=data['SYMPTOM_TEXT'].str.contains("|".join(keywords))
# Check values in the Covid column.
print(data['Covid'].unique())

# Explore new data frame.
print(data.tail(10))
print(data.describe())
print(data.shape)

# Create a new dataset that contains only Covid related data.
covidData = data.loc[data['Covid']==True]
print( covidData.describe())
print(covidData.shape)
print(covidData.tail(10))

# Generate output of covid dataset to a new CSV file.
covidData.to_csv('./data/VAERSData/2021VAERSData_covid.csv')
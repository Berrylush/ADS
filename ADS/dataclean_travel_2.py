# -*- coding: utf-8 -*-
"""ADS Exp 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bUGl69DjjSi9sw8uol1FMhYYbgOO4Njq
"""

# https://openmv.net/info/travel-times

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/sample_data/travel-times.csv')
df.head(10)

df = df[df['FuelEconomy'] != '-']

df.head(10)

df.drop(['Date', 'StartTime'], axis =1)

df.isnull().mean()
# gives percentage of null values in particular column

"""# deletion of rows with missing data

"""

remove_na_rows = df.dropna(axis = 0)
print(remove_na_rows.shape)
print(df.shape)

"""# Mean/Median imputation

"""

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
imputer = imputer.fit(df[['FuelEconomy']])
data = imputer.transform(df[['FuelEconomy']])
for i in range(0, 10):
  print(data[i])

median_fuelEconomy = df['FuelEconomy'].median()
print(df['FuelEconomy'].fillna(median_fuelEconomy))

# Mode imputation, Arbitrary value imputation

# list comprehension to get all categorical variables
cat_variables = [ var for var in df.columns if len(df[var].unique()) < 10]
cat_variables

"""# Mode imputation / frequent category Imputation

"""

mode_comments = df['Comments'].mode()
print(df['Comments'].fillna(mode_comments[0]))

"""# Arbitrary value imputation from values in column

"""

print(df['Comments'].fillna('Rain, rain, rain'))

"""# Random Sample Imputation / Add a new Cateogory as missing"""

print(df['Comments'].fillna('Missing'))

# fuelEconomy is numerical column
# df['FuelEconomy']
#compute the mean of Boolean mask (True evaluates as 1 and False as 0)
na_variables = [ var for var in df.columns if df[var].isnull().mean() > 0 ]
na_variables

# list comprehension to get all numerical variables
num_variables = [ var for var in df.columns if len(df[var].unique()) > 10]
num_variables

from sklearn.linear_model import LinearRegression

linear_regressor = LinearRegression()  
X = np.array(df['Distance']).reshape(-1, 1)
y = np.array(df['TotalTime']).reshape(-1, 1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
  
# Splitting the data into training and testing data
regr = LinearRegression()
  
regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))

y_pred = regr.predict(X_test)
plt.scatter(X_test, y_test, color ='b')
plt.plot(X_test, y_pred, color ='k')
  
plt.show()

df['AvgSpeed'].plot.density(color='green')
plt.title('Density plot for Speeding')
plt.show()


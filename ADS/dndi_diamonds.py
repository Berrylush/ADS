# -*- coding: utf-8 -*-
"""ADS Exp 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yHTSpDfc1sd5J3HSValB2d9iKjaJUxpn
"""

# https://www.kaggle.com/datasets/shivam2503/diamonds?resource=download

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/sample_data/diamonds.csv')

# cut quality of the cut (Fair, Good, Very Good, Premium, Ideal)
# color diamond colour, from J (worst) to D (best)
# clarity a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))

# price price in US dollars (\$326--\$18,823)
# carat weight of the diamond (0.2--5.01)
# x length in mm (0--10.74)
# y width in mm (0--58.9)
# z depth in mm (0--31.8)
# depth total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43--79)
# table width of top of diamond relative to widest point (43--95)

df.head(5)

df = df.drop('Unnamed: 0', axis = 1)

df.describe()

df.isnull().any()

print(df['price'].median())
print(df['price'].max())
print(df['price'].min())

df_numerics_only = df.select_dtypes(include=np.number)
df_numerics_only

df_numerics_only.median()

print(df['price'].mode())
print(df['cut'].mode())
print(df['color'].mode())

df_numerics_only.mean()

#Standard error of mean
df_numerics_only.sem()

df_numerics_only.skew()

#kurtosis
sr = pd.Series(df['price'])
print(sr.kurtosis())

df_numerics_only.var()

df_numerics_only.std()

import seaborn as sns
corr = df_numerics_only.corr()
sns.heatmap(corr, cmap="Blues", annot=True)

g=sns.distplot(df['price'])

plt.scatter(df['carat'], df['price'])
plt.show()

df['x'] = df['x'].clip(lower=3, upper=10)
plt.scatter(df['x'], df['price'])
plt.show()

df['y'] = df['y'].clip(lower=3, upper=10)
plt.scatter(df['y'], df['price'])
plt.show()

df['z'] = df['z'].clip(lower=0, upper=10)
plt.scatter(df['z'], df['price'])
plt.show()

plt.boxplot(df['price'])
plt.show()

plt.boxplot(df['depth'])  # (43--79)
plt.show()

# (43--95)
plt.boxplot(df['table'])
plt.show()

from scipy import stats
stats.trim_mean(df['price'], 0.1)

df['price'].mean()

#Frequency
count = df['cut'].value_counts()
print(count)

sns.histplot(data=df, x='y', kde=True)

import plotly.express as px

fig = px.scatter(df, x="x", y="y",
                 size='z', 
                 hover_data=['z'])

fig.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/sample_data/mushrooms.csv')
df.head(5)

sns.pairplot(df)


# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KHfakhAoT5qnHOshV7kVyED88jxXumCM
"""

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

data = pd.read_csv('Iris.csv')
data.head()

new_data=data.drop(['Id'],axis=1)
new_data.boxplot()

# create arrays
X = df.values

# instantiate model
nbrs = NearestNeighbors(n_neighbors = 3)

# fit model
nbrs.fit(X)

# input data
df = data[["SepalLengthCm", "SepalWidthCm"]]
# scatterplot of inputs data

plt.scatter(df["SepalLengthCm"], df["SepalWidthCm"])

# distances and indexes of k-neaighbors from model outputs
distances, indexes = nbrs.kneighbors(X)
# plot mean of k-distances of each observation

plt.plot(distances.mean(axis =1))

# visually determine cutoff values > 0.15
outlier_index = np.where(distances.mean(axis = 1) > 0.15)
outlier_index

# filter outlier values
outlier_values = df.iloc[outlier_index]
outlier_values

# plot data
plt.scatter(df["SepalLengthCm"], df["SepalWidthCm"], color = "b", s = 65)
# plot outlier values
plt.scatter(outlier_values["SepalLengthCm"], outlier_values["SepalWidthCm"], color = "r")

# data wrangling
import pandas as pd
# visualization
import matplotlib.pyplot as plt
# algorithm
from sklearn.cluster import DBSCAN

# input data
df = data[["SepalLengthCm", "SepalWidthCm"]]
# specify & fit model
model = DBSCAN(eps = 0.4, min_samples = 10).fit(df)

# visualize outputs
colors = model.labels_
plt.scatter(df["SepalLengthCm"], df["SepalWidthCm"], c = colors)

# outliers dataframe
outliers = df[model.labels_ == -1]
print(outliers)


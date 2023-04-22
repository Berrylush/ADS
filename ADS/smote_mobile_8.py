# -*- coding: utf-8 -*-
"""ADS Exp8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bTzqe-uY_9AtF4Ufcr0zQDv1A2gGxP74
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/sample_data/Mobile-Company-Telco-Customer-Churn.csv')
df.head(5)

df = df.drop(['customerID', 'TotalCharges'], axis = 1)

df.info()

from sklearn.preprocessing import LabelEncoder

# df['StreamingMovies'].dtype
for col in df.columns:
  if df[col].dtype == 'O':
    label_encode = LabelEncoder()
    df[col] = label_encode.fit_transform(df[col])
df

df['Churn'].value_counts()

sns.countplot(x ='Churn', data = df)

X = df.drop('Churn', axis = 1)
y = df['Churn']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

pred = tree.predict(X_test)

# print(y_test)
y_test.value_counts()

# print(pred)
left_customers = X_test.loc[y_test == 1]
print(len(left_customers))
plt.hist(left_customers['MonthlyCharges'])
plt.show()

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

from imblearn.over_sampling import SMOTE
sm = SMOTE(sampling_strategy='auto', k_neighbors=2, random_state=84)
X_res, y_res = sm.fit_resample(X_train, y_train)

tree.fit(X_res, y_res)

pred_res = tree.predict(X_test)

print(accuracy_score(y_test, pred_res))
print(classification_report(y_test, pred_res))
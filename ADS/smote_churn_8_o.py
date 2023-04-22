# -*- coding: utf-8 -*-
"""SMOTE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PtpyZTirJTISqsw3KKohicy0Whiipix9
"""

from imblearn.over_sampling import SMOTE
from matplotlib import pyplot
from numpy import where
import pandas as pd

df = pd.read_csv('Churn_Modelling.csv')
df.head()

import seaborn as sns

data = df[['CreditScore', 'Age', 'Exited']]
print(data.head(10))
sns.scatterplot(data = data, x ='CreditScore', y = 'Age', hue = 'Exited')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
#Splitting the data with stratification
X_train, X_test, y_train, y_test = train_test_split(data[['CreditScore', 'Age']], df['Exited'], test_size = 0.2, stratify = df['Exited'], random_state = 101)

smote = SMOTE(random_state = 101)
X_oversample, y_oversample = smote.fit_resample(X_train, y_train)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

print(classification_report(y_test, classifier.predict(X_test)))

classifier_o = LogisticRegression()
classifier_o.fit(X_oversample, y_oversample)
print(classification_report(y_test, classifier_o.predict(X_test)))

smote = SMOTE(random_state = 101)
X, y = smote.fit_resample(df[['CreditScore', 'Age']], df['Exited'])
#Creating a new Oversampling Data Frame
df_oversampler = pd.DataFrame(X, columns = ['CreditScore', 'Age'])
df_oversampler['Exited']=y
print(df_oversampler.head())

sns.countplot(data=df_oversampler,x='Exited')

from collections import Counter
X=df[['CreditScore', 'Age']]
y=df['Exited']

oversample = SMOTE()
X, y = oversample.fit_resample(X, y)
# summarize the new class distribution
counter = Counter(y)
print(counter)

sns.scatterplot(data = df_oversampler, x ='CreditScore', y = 'Age', hue = 'Exited')
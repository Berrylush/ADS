# -*- coding: utf-8 -*-
"""ADS Exp 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UahLMnCtSvcGgAGu0GCPzRuxPrC9vIYC
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# from google.colab import drive
# drive.mount('/content/drive')

df = pd.read_csv('/content/sample_data/Mobile-Company-Telco-Customer-Churn.csv', delimiter = ',')
pd.pandas.set_option('display.max_columns', None)

df.head(5)

df = df.drop(['customerID'], axis=1)

df.head(5)

df.isnull().sum()

df.dtypes

from sklearn.preprocessing import LabelEncoder 
lbe = LabelEncoder()

cat_cols = [col for col in df.columns if df[col].dtype=="O"]
print(cat_cols)
for col in cat_cols:
  if len(df[col].unique()) < 10:
    df[col]= lbe.fit_transform(df[col])
  else:
    df = df.drop(col, axis = 1)

df

df.dtypes

X = df.drop('Churn', axis = 1)
y = df['Churn']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm_arr = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(tn)
print(fp)
print(fn)
print(tp)

df_cm = pd.DataFrame(cm_arr, index = [i for i in "01"],
                  columns = [i for i in "01"])
plt.figure(figsize = (7,5))
sns.heatmap(df_cm, annot=True)

"""## Accuracy"""

accuracy = (tp + tn) / (tp + tn + fp + fn)
accuracy

"""## Error Rate"""

error_rate = (fp + fn) / (tp + tn + fp + fn)
error_rate

"""## Precision"""

precision = (tp) / (tp + fp)
precision

"""## Sensitivity"""

sensitivity = (tp) / (tp + fn)
sensitivity

"""## Specificity"""

specificity = (tn) / (tp + fp)
specificity

"""## ROC"""

import math
ROC = math.sqrt(sensitivity ** 2 + specificity ** 2) / math.sqrt(2)
ROC

"""## F1 Score"""

f1_score = (2 * precision * sensitivity) / (precision + sensitivity)
f1_score

"""## Geometric Mean"""

geometric_mean = math.sqrt(sensitivity * specificity)
geometric_mean

"""## False Positive Rate"""

fpr = 1 - specificity
fpr

"""## False Negative Rate"""

fnr = 1 - sensitivity
fnr

"""## ROC Curve"""

import matplotlib.pyplot as plt
from sklearn import metrics
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred, pos_label=0)
print(fpr)
auc = metrics.roc_auc_score(y_test, y_pred)

plt.plot(fpr,tpr, label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()

"""# Logistic Regression"""

df = pd.read_csv('/content/sample_data/Salary_Data.csv')

# df.head(5)
print(df.shape)
X = df['YearsExperience']
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
X_train= X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
y_pred

y_mean = sum(y) / len(y)
x_mean = sum(X) / len(X)

"""## Karl Pearson's Coefficient"""

x2 = 0
for val in X:
  x2 += (val - x_mean) * (val - x_mean)

y2 = 0
for val in y:
  y2 += (val - y_mean) * (val - y_mean)

num = 0
for i, j in zip(X, y):
  num += (i - x_mean) * (j - y_mean)

r = num / (math.sqrt(x2 * y2))
print(r)

"""## Coefficient of Determination"""

from sklearn.metrics import r2_score, mean_squared_error
R_sq = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(mse)

"""##Mean Squared Error"""

mse = 0

for i , j in zip(y_test, y_pred):
  mse += (i - j) * (i - j)

print(mse / len(y_test))

"""## Root mean squared error"""

root_mean_sq_error = math.sqrt(mse)
print(root_mean_sq_error)

"""## Root mean squared relative error

"""

rmser = 0

for i,j in zip(y_test, y_pred):
  rmser += ((i - j) / i) ** 2

rmser = math.sqrt(rmser / len(y_test))
print(rmser)

"""## Mean Absolute error"""

mae = 0
for i,j in zip(y_test, y_pred):
  mae += abs(i - j)

mae = mae / len(y_test)
print(mae)

"""## Mean Absolute Percentage Error"""

mape = 0
for i,j in zip(y_test, y_pred):
  mape = abs((i - j) / i)

mape = (mape / len(y_test)) * 100
print(mape)
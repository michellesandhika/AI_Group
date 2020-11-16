import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
import sklearn.metrics as metrics
import math
import seaborn as sns


## input the data

test_data = pd.read_csv("test.csv")
train_data = pd.read_csv("train.csv")

## present the data

print(train_data["SalePrice"].describe())
sns.distplot(train_data['SalePrice'])
plt.show()

## select variables, find collinearity

corr_matrix = train_data.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corr_matrix, mask = mask, cmap = cmap, vmax = 1, center = 0, square=True, linewidths=.5, cbar_kws={"shrink":.5})
plt.show()
## what to do with missing values


## 

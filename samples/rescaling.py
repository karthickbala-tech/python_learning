import numpy as np
import pandas as pd
from sklearn import preprocessing
feature = np.array([[-500.5],
                    [-100.1],
                    [0],
                    [100.1],
                    [900.9]])
minmax_scale=preprocessing.MinMaxScaler(feature_range=(0,1))
scaled_feature=minmax_scale.fit_transform(feature)
#print(scaled_feature)

x = np.array([[-1000.1],
        [-200.2],
        [500.5],
        [600.6],
        [9000.9]])
scaler=preprocessing.StandardScaler()
standardized=scaler.fit_transform(x)
#print(standardized)

features = np.array([[0.5, 0.5],
                    [1.1, 3.4],
                    [1.5, 20.2],
                    [1.63, 34.4],
                    [10.9, 3.3]])
normalizer=preprocessing.Normalizer(norm="l2")
b=normalizer.transform(features)
#print(b)

featuress = np.array([[2, 3],
                    [2, 3],
                    [2, 3]])
def add_ten(x):
    return x + 10
ten_transformer = preprocessing.FunctionTransformer(add_ten)
a=ten_transformer.transform(featuress)
#print(a)

#LINEAR REGRESSION
#Fitting a line
 
'''from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

boston=load_boston()
fearure =boston.data[:,0:2] 
target= boston.target
regression=LinearRegression()
print(regression)
model=regression.fit(features,target)
#print(model)'''

from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

# Load California housing dataset
housing = fetch_california_housing()
features = housing.data[:, 0:2]  # Use first two features
target = housing.target

# Create and fit the linear regression model
regression = LinearRegression()
model = regression.fit(features, target)

# Print model coefficients
print(regression)
print(model)


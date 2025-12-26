import pandas as pd 
url='/home/parrot/ml-env/customers-100.csv'
df=pd.read_csv(url)

#drop dublicate
print(df.drop_duplicates(subset=['First Name'],keep='last'))

#seelecting rows based on conditionals
print(df[df['country']=='chile'])

#navigating dataframe
print(df.iloc[0])
print(df.iloc[0:5])
df=df.set_index(df['First Name'])
print(df.loc['Sheryl'])
# 
#shape
print(df.shape)

#describe
print(df.describe())

#creat row
new_person=df.series()

#append row
df.append(new_person,ignore_index=True)

#head and tail
print(df.head(5))
print(df.tail(5))

#rescaling a Feture
import pandas as pd
import numpy as np

# Load libraries
from sklearn import preprocessing

# Create feature
feature = np.array([[-500.5],
                    [-100.1],
                    [0],
                    [100.1],
                    [900.9]])
# Create scaler
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
# Scale feature
scaled_feature = minmax_scale.fit_transform(feature)

print(scaled_feature)

# Load libraries
import numpy as np
from sklearn import preprocessing

# Create feature
x = np.array([[-1000.1],
        [-200.2],
        [500.5],
        [600.6],
        [9000.9]])

# Create scaler
scaler = preprocessing.StandardScaler()

# Transform the feature
standardized = scaler.fit_transform(x)

print(standardized)


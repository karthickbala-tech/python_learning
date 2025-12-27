import pandas as pd

# creating dataframe using dic
employees = {
    "Ali": {"marks": 85, "job": "Data Analyst"},
    "Sara": {"marks": 92, "job": "ML Engineer"},
    "John": {"marks": 78, "job": "Web Developer"}
}
print(pd.DataFrame(employees))

# to convert dataframe to csv
employees = {
    "Ali": {"marks": 85, "job": "Data Analyst"},
    "Sara": {"marks": 92, "job": "ML Engineer"},
    "John": {"marks": 78, "job": "Web Developer"}
df=pd.DataFrame(employees)
print(df.to_csv())

# import csv file using read_csv and acessing methods
df = pd.read_csv("/home/parrot/Documents/machine_learning/ml_icanio/customers-100.csv")

print(df.head)
print(df.tail(5))
print(df.describe)
print(df.describe())
print(df.info)
print(df.info())
print(df['Customer Id'][50])
print(df.isnull().sum())
print(df.isnull().any)



# series -> 1 dimention table
Series=pd.Series([1,2,3,4])
Series.index=range(1,len(Series)+1)
print(Series)

# Dataframe 2 dimention table using dictinory
Dataframe=pd.DataFrame({'name':['raja','bala','magesh','harish'],'age':[23,32,12,33],'mark':[78,97,78,56]},index=pd.RangeIndex(start=1,stop=5))
print(Dataframe)

# Dataframe 2 dimention table using list
data = [["Raja", 22, 85],["Karthick", 24, 90],["Arun", 23, 88]]
df = pd.DataFrame(data, columns=["Name", "Age", "Score"])
print(df)

# dataframe info
Dataframe=pd.DataFrame({'name':['raja','bala','magesh','harish'],'age':[23,32,12,33],'mark':[78,97,78,56]},index=pd.RangeIndex(start=1,stop=5))
print(Dataframe.shape)
print(Dataframe.columns)
print(Dataframe.dtypes)

# Dataframe acessing 
Dataframe=pd.DataFrame({'name':['raja','bala','magesh','harish'],'age':[23,32,12,33],'mark':[78,97,78,56]},index=pd.RangeIndex(start=1,stop=5))
print(Dataframe["age"])
print(Dataframe[['age','mark']])

# Select row by position
print(Dataframe['age'].iloc[1])

# Select a row (by index)
print(Dataframe['age'].loc[1])

Dataframe["Passed"] = Dataframe["mark"] > 75
print(Dataframe)


# Detect Missing Values
print(df.isnull())
print()
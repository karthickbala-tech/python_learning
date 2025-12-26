import numpy as np

#list vs numpy array
# List=[1,2,3,4,5]
# numpy_array=np.array([1,2,4,5,3,5])
# print(List)
# print(numpy_array)

# arange and reshape
# x=np.arange(10).reshape((5,2))
# y=range(5)
# print(x)
# print(list(y))

#Creating Arrays with Zeros
# zeros_arr= np.zeros((3,2))
# print(zeros_arr)

#Creating Arrays with Ones
# once_arr= np.ones((4,3))
# print(once_arr)

#Creating Range of Numbers
# numpy_range=np.arange(2,7)
# print(numpy_range

#Evenly Spaced Numbers
# space_numbers=np.linspace(1,10,1000)
# print(space_numbers)

# changeing data types
# num_dtype=np.array([1.0,3.9])
# num_dtype=num_dtype.astype(float)
# print(num_dtype)

#dimension
# a = np.array([1, 2, 3, 4])
# b = np.array([[1, 23, 3],[3, 4, 5]])
# c = np.array([[[1, 2, 4],[3, 4, 5]]])

# print(a)
# print(b)
# print(c)

#2d slicing
# arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# # print(arr[:2, :2])

#boolean indexing
# arr = np.array([10, 25, 30, 15, 5])
# filtered = arr[arr > 15]
# print(filtered)

#Aggregation Functions
# arr=np.array([1,2,3,4,5,6])
# print(arr.min())
# print(arr.max())
# print(arr.mean())
# print(arr.sum())

# #Axis Concept
# dim_array=np.array([[1,2,4,5],[23,5,3,6]])
# print(dim_array.sum(axis=1))


# dim_array=np.array([[1,2,4,5],[23,5,3,6]])
# print(dim_array.sum(axis=0))

#array vs list
# arr=[1,2,3]
# result = []
# for i in arr:
#     result.append(i * 2)
# print(result)
# arr=np.array([1,2,3,])

#martix multiplication
# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[8,9]])
# # print(a@b)
# print(a.T)
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr) #remodelar 4 array de 3 elementos c/u


arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr1.reshape(2, 3, 2)

print(newarr)



arr2 = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr2.reshape(-1)
print(' array 2d',arr2)
print( 'array 1d',newarr)
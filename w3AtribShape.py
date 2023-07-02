import numpy as np

#Devuelve una tupla con las dimensiones del array a.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) 
print(arr) # dos dimensiones: dos elementos la primera y 4 elementos la segunda


arr1 = np.array([1, 2, 3, 4,5], ndmin=7)
print(arr1)
print('shape of array :', arr1.shape)



#NumPy Data Types

import numpy as np

arr = np.array([1, 2, 3, 4])
print('devuelve el tipo de dato del array:',arr.dtype)

arr1 = np.array([1, 2, 3, 4], dtype='U')
print(arr1)
print(arr1.dtype) #cambia el tipo de dato

#arr2 = np.array(['a', '2', '3'], dtype='i')
#si hay un tipo distinto, hay ValueError

arr3 = np.array([1.1, 2.1, 3.1])

newarr = arr3.astype(int) #o i

print(newarr)
print('nuevo tipo:',newarr.dtype)


''' tipo de  datos
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fi'''




import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print('arreglo modificado',arr)
print('arreglo copiado',x)


arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42  #se cambia el original

print(arr)
print(x)  #se modifican los dos


arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31 #se cambia el view

print(arr)
print(x)



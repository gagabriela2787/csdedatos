import numpy as np


arr = np.array([1, 2, 3])
for x in arr:
  print(x) #iterar en un array 1d

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr2:
  print(x) #iterar los elementos de 2D

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr3:
  for y in x:
    print(y) #iterar cada valor de cada elemento


arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr4:
  print(x) #iterar en 3D

arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr5:
  for y in x:
    for z in y:
      print(z) #iterar cada valor de cada elemento


#funcion nditer()
arr6 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr6):
  print(x)


arr7 = np.array([1, 2, 3])
for x in np.nditer(arr7, flags=['buffered'], op_dtypes=['S']):
  print(x) #iterar con otro  tipo de dato

arr8 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr8[:, ::2]):
  print(x)



#enumerar la iteracion, saber el indice del elemento


arr9 = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr9):
  print(idx, x)


arr10 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr10):
  
 print(arr10)
 print(idx, x)
  



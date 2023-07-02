import numpy as np


arr =np.array([1,2,3,4,5]) #metodo para crear una array #1D
print(arr)

print(type(arr)) #clase = type

arr1= np.array(42)  #0D
print(arr1)


matrix=np.array([[1,2,3],[4,5,6]])  #2D
print(matrix)


arreglo3=np.array([matrix,matrix]) #matriz de la matriz anterior
print(arreglo3)


arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr2)  #3D



a=np.arange(1,11)  #uso de arange
print(a)

matriz= np.arange(1,10).reshape(3,3)
print(matriz)


print("nombre:",matriz.ndim) #dimension y nombre
print(matriz.ndim) #dimension
print("shape",matriz.shape)
print("size",matriz.size)


array = np.array([1,2,3,4], ndmin=5) #crea un array 5D
print(array)
print('la dimension es', array.ndim)# muestra la dimension


ga= np.arange(1,11)
print(ga)
print("ndim:",ga.ndim)
print("shape",ga.shape)
print("size",ga.size)



#Access Array Elements
arr4 = np.array([1, 2, 3, 4])
print(arr4[0])

arr3 = np.array([1, 2, 3, 4])
print(arr3[3])
print(arr3[1], arr3[3]) #acceder a dos elementos 1D


#acceder a un elemento de un array 2D
arr5= np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('el tercer elemento array 2D: ', arr5[1, 3]) #0 para primer columna


#acceder a un elemnto de un array 3D
arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr6)
print(arr6[1, 0, 2])



#se usa negativo para acceder desde el final
arr7 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('de atras hacia adelante: ', arr7[1, -5])



#slice 1D
arr8 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr8[1:]) #todo desde el 1
print(arr8[:3]) #todo hasta el 3
print(arr8[:])#todo

#slice 2D
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('slice 2D',arr[1, 1:4])

#slice negativo
arr9= np.array([1, 2, 3, 4, 5, 6, 7])
print(arr9[-5:-2])  #muestra 3 ,4 y 5.-

#de ambos, devuelve el 2
arr10 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr10)
print('elementos 2',arr10[0:2, 2])

#devuelve un array 2d, mas chico
arr11 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('array entero',arr11)
print(arr[0:2, 1:4])





#step
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::3]) #salta de 3 en 3 en todo el array






#creando un arreglo con 0

arreglo=np.zeros((10))
#print(arreglo)

arreglo=np.zeros((3,6))#cero
#print(arreglo)

arreglo=np.ones((2,3)) #uno
#print(arreglo)


#creando un arreglo con un mismo numero
arrerre=np.full(10,5)
#print(arrerre)

#crear un arreglo con valores uniformemente espaciados
arregli=np.linspace(1,2,10)
print(arregli)


#nros aleatorios entre 0 y 1
b=np.random.randint(0,100,size=10)
#print(b)


#nros aleatorios entre 0 y 1
b=np.random.rand(25)
#print(b)






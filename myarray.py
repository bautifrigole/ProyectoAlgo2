from algo1 import *

def access(array, position): # 3
	return array[position] # 3

# Devuelve el índice donde se encuentra la primera instancia del elemento
def search(array, element): # 1+2
	for i in range(len(array)): # 2*n + n*s = 12n
		if array[i] == element: # 6+1
			return i # 3 -> s=10
	return # 1

# Inserta un elemento en una posición determinada de un Array
# Salida: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento, sino None
def insert(array, element, position): # 1+3
	if position >= len(array): return # 1+2+1 = 4
	if type(element) != type(array[0]): return # 1+2+2+1+1 = 7
	
	for i in range(position, len(array)): # 2*n+ n*10
		if i == position: # 1
			oldValue = array[i] # 2
			array[i] = element # 2
		else: 
			value = oldValue # 1
			oldValue = array[i] # 2
			array[i] = value # 2
	return position # 3

# Elimina un elemento del arreglo
# Salida: Devuelve la posición donde se encuentra el elemento a eliminar, sino None
def delete(array, element): # 1+2
	position = search(array, element) # 1+(4+12n)
	if position == None: return # 2
	if type(element) != type(array[0]): return # 1+2+3+1

	for i in range(position, len(array)): # 2n+13n
		if i+1 < len(array): #1+1+1+1
			array[i] = array[i+1] # 1+2+2+1
		else:
			array[i] = None # 1+1+1
	return position # 1+2

# Devuelve el número de elementos distintos a None
def length(array): # 1+1
	count = 0 # 1
	for i in range(len(array)): # 2n+5n
		if array[i] != None: # 1+2
			count += 1 # 2
	return count # 3


def copy_array_without_nones(array, length):
	new_array = Array(length, array[0])
	index = 0
	for i in range(len(array)):
		if array[i] is not None:
			new_array[index] = array[i]
			index += 1
	return new_array

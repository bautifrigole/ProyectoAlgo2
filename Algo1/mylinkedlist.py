from Algo1.myarray import Array


class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None


# Agrega un elemento al comienzo de lista
# Salida: ​ No hay salida definida
def add(L, element):
    current = L.head
    newNode = Node()
    newNode.value = element

    if current == None:
        L.head = newNode
    else:
        newNode.nextNode = current
        L.head = newNode
    return


# Agrega un nodo al comienzo de lista
# Salida: ​ No hay salida definida
def addNode(L, node):
    current = L.head

    if current == None:
        L.head = node
    else:
        node.nextNode = current
        L.head = node
    return


# Descripción: ​Busca un elemento de la lista
# Salida​: Devuelve la posición donde se encuentra la primera instancia del elemento, Devuelve None​ si el elemento no se encuentra.
def search(L, element):
    current = L.head
    currentPos = 0

    while current != None:
        if current.value == element:
            return currentPos

        current = current.nextNode
        currentPos += 1
    return


# Descripción: ​Busca un elemento de la lista
# Salida​: Devuelve la posición donde se encuentra la primera instancia del elemento, Devuelve None​ si el elemento no se encuentra.
def searchNode(L, node):
    current = L.head
    currentPos = 0

    while current != None:
        if current == node:
            return currentPos

        current = current.nextNode
        currentPos += 1
    return


# Descripción:​ Inserta un elemento en una posición determinada de la lista que representa el TAD​ ​secuencia​.
# Salida​: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento. En caso contrario devuelve ​None​. Devuelve None si la posición a insertar es mayor que el número de elementos en la lista.
def insert(L, element, position):
    current = L.head
    currentPos = 0

    if position == 0:
        add(L, element)
        return position

    elif position > 0:
        if current == None: return
        newNode = Node()
        newNode.value = element

        while current.nextNode != None:
            if currentPos + 1 != position:
                current = current.nextNode
                currentPos += 1
            else:
                newNode.nextNode = current.nextNode
                current.nextNode = newNode
                return position
        current.nextNode = newNode
        return currentPos + 1
    return


# Descripción:​ Inserta un nodo en una posición determinada de la lista que representa el TAD​ ​secuencia​.
# Salida​: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento. En caso contrario devuelve ​None​. Devuelve None si la posición a insertar es mayor que el número de elementos en la lista.
def insertNode(L, node, position):
    current = L.head
    currentPos = 0

    if position == 0:
        addNode(L, node)
        return position

    elif position > 0:
        if current == None: return

        while current.nextNode != None:
            if currentPos + 1 != position:
                current = current.nextNode
                currentPos += 1
            else:
                node.nextNode = current.nextNode
                current.nextNode = node
                return position
        current.nextNode = node
        return currentPos + 1
    return


# Elimina un elemento de la lista
# Poscondición:​ Se debe desvincular el ​ Node​ a eliminar.
# Salida​ : Devuelve la posición donde se encuentra el elemento a eliminar. Devuelve ​ None​ si el elemento a eliminar no se encuentra
def delete(L, element):
    current = L.head
    position = search(L, element)
    if position == None: return
    if position == 0:
        L.head = L.head.nextNode
        return position

    for i in range(0, position - 1):
        current = current.nextNode
    current.nextNode = current.nextNode.nextNode
    return position


# Elimina un nodo de la lista
# Poscondición:​ Se debe desvincular el ​Node​ a eliminar.
# Salida​ : Devuelve la posición donde se encuentra el elemento a eliminar. Devuelve ​ None​ si el elemento a eliminar no se encuentra
def deleteNode(L, node):
    current = L.head
    position = searchNode(L, node)
    if position == None: return
    if position == 0:
        L.head = L.head.nextNode
        return position

    for i in range(0, position - 1):
        current = current.nextNode
    current.nextNode = current.nextNode.nextNode
    return position


# Elimina un elemento por posición de la lista
# Poscondición:​ Se debe desvincular el ​ Node​ a eliminar.
# Salida​ : Devuelve la posición donde se encuentra el elemento a eliminar. Devuelve ​ None​ si el elemento a eliminar no se encuentra
def deletePosition(L, position):
    current = L.head
    node = accessNode(L, position)
    if node == None: return
    if position == 0:
        L.head = L.head.nextNode
        return position

    for i in range(0, position - 1):
        current = current.nextNode
    current.nextNode = current.nextNode.nextNode
    return position


# Calcula el número de elementos de la lista
# Salida​ : Devuelve el número de elementos.
def length(L):
    current = L.head
    currentPos = 0

    while current != None:
        current = current.nextNode
        currentPos += 1
    return currentPos


# Permite acceder a un elemento de la lista en una posición determinada.
# Salida​: Devuelve el valor de un elemento en una position de la lista, devuelve​ None​ si no existe elemento​ para dicha posición.
def access(L, position):
    if position >= 0:
        current = L.head

        for i in range(0, position):
            if current == None: return
            current = current.nextNode
        return current.value
    return


# Permite acceder a un elemento de la lista en una posición determinada.
# Salida​: Devuelve el valor de un elemento en una position de la lista, devuelve​ None​ si no existe elemento​ para dicha posición.
def accessNode(L, position):
    if position >= 0:
        current = L.head

        for i in range(0, position):
            if current == None: return
            current = current.nextNode
        return current
    return


# Permite cambiar el valor de un elemento de la lista en una posición determinada
# Salida​ : Devuelve ​ None si no existe elemento ​ para dicha posición. Caso contrario devuelve la posición donde pudo hacer el update.
def update(L, element, position):
    if position >= 0:
        current = L.head

        for i in range(0, position):
            current = current.nextNode
            if current == None: return
        current.value = element
        return position
    return


def revert(L):
    newL = LinkedList()
    len = length(L)
    current = L.head

    for i in range(len):
        len -= 1
        add(newL, current.value)
        current = current.nextNode
    return newL


def print_list(L):
    if L is None:
        print("List is None")
        return
    current = L.head
    currentPos = 0

    while current != None:
        if currentPos != 0: print(end=" -> ")
        print(current.value, end="")
        current = current.nextNode
        currentPos += 1
    print()
    return currentPos


from random import randint


def random_list(length, rnd_from, rnd_to):
    L = LinkedList()
    for i in range(length):
        add(L, randint(rnd_from, rnd_to))
    return L


def moveNode(L, position_orig, position_dest):
    if position_orig == position_dest:
        return
    elif position_orig == 0:
        # La head es la posición de origen
        originalNode = L.head

        L.head = L.head.nextNode
        previousDest = previousNode(L, position_dest)

        originalNode.nextNode = previousDest.nextNode
        previousDest.nextNode = originalNode
    elif position_dest == 0:
        # La head es la posición de destino
        previousOrig = previousNode(L, position_orig)
        originalNode = previousOrig.nextNode

        if previousOrig.nextNode != None:
            previousOrig.nextNode = previousOrig.nextNode.nextNode
        else:
            previousOrig.nextNode = None

        originalNode.nextNode = L.head
        L.head = originalNode
    else:
        previousOrig = previousNode(L, position_orig)
        originalNode = previousOrig.nextNode

        if previousOrig.nextNode != None:
            previousOrig.nextNode = previousOrig.nextNode.nextNode
        else:
            previousOrig.nextNode = None

        previousDest = previousNode(L, position_dest)
        originalNode.nextNode = previousDest.nextNode
        previousDest.nextNode = originalNode


def previousNode(L, position):
    count = 0
    current = L.head
    while count < position - 1:
        current = current.nextNode
        count += 1
    return current


def swapNodes(list, nodeAPos, nodeBPos):
    nodeB = accessNode(list, nodeBPos)

    moveNode(list, nodeAPos, nodeBPos)
    nodeBnewPos = searchNode(list, nodeB)
    moveNode(list, nodeBnewPos, nodeAPos)


def is_sublist(list1, list2):
    node1 = list1.head
    while node1 is not None:
        if search(list2, node1.value) is None:
            return False
        node1 = node1.nextNode
    return True


def are_same_list(list1, list2):
    node1 = list1.head
    node2 = list2.head
    while node1 is not None:
        if node2 is None or node1.value != node2.value:
            return False
    return True


def array_to_list(array):
    L = LinkedList()
    for i in range(len(array)-1, -1, -1):
        add(L, array[i])
    return L


def list_to_array(list, n):
    node = list.head
    if node is None:
        return
    array = Array(n, node.value)
    for i in range(n):
        array[i] = node.value
        node = node.nextNode
    return array


def concat_list(L1, L2):
    if L1 is None:
        if L2 is None:
            return LinkedList()
        else:
            return L2

    node = L1.head
    if node is not None:
        while node.nextNode is not None:
            node = node.nextNode
        if L2 is not None:
            node.nextNode = L2.head
        return L1
    else:
        if L2 is None:
            return L1
        else:
            return L2

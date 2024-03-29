from ship import Ship
from Algo1.algo1 import Array
from Algo1.myarray import copy_array_without_nones


def create_index(path):
    with open(path) as f:
        lines = f.readlines()

    ships = Array(len(lines) - 1, Ship())
    length_ships = 0
    for i in range(0, len(lines) - 1):
        if not is_blank_str(lines[i + 1]):
            index = 0
            data = Array(4, "")
            # Inicializamos con ""
            data.data = ["", "", "", ""]
            for j in range(len(lines[i + 1])):
                if lines[i + 1][j] != " " and lines[i + 1][j] != "\n":
                    data[index] += lines[i + 1][j]
                else:
                    index += 1
            ships[i] = Ship(data[0], [int(data[1]), int(data[2])], data[3])
            length_ships += 1
    ships = copy_array_without_nones(ships, length_ships)
    return ships


def is_blank_str(string):
    for i in range(len(string)):
        if string[i] != " " and string[i] != "" and string[i] != "\n":
            return False
    return True

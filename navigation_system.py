import math
from copy import deepcopy
from ship import *
from algo1 import Array
from myarray import copy_array_without_nones
from mylinkedlist import LinkedList, add, list_to_array, concat_list


def create_index(path):
    with open(path) as f:
        lines = f.readlines()

    ships = Array(len(lines) - 1, Ship())
    length_ships = 0
    for i in range(0, len(lines)-1):
        if lines[i+1].strip() != "":
            index = 0
            data = ["", "", "", ""]
            for j in range(len(lines[i + 1])):
                if lines[i + 1][j] != " " and lines[i + 1][j] != "\n":
                    data[index] += lines[i + 1][j]
                else:
                    index += 1
            ships[i] = Ship(data[0], [int(data[1]), int(data[2])], data[3])
            length_ships += 1
    a = copy_array_without_nones(ships, length_ships)
    return a

#TODO: Probar

def search(ships, date, name,initial_day):
    actual_day = get_day(date)
    if actual_day is not None:
        ship = try_search_ship_by_name(ships, name)
        ship.update_position(actual_day,initial_day)
        return ship.actual_position


def get_day(date):
    day_month = ["", ""]
    index = 0
    for i in range(len(date)):
        if date[i] != "-":
            day_month[index] += date[i]
        else:
            index += 1
            if index == 2:
                break

    day_month[0] = int(day_month[0])
    day_month[1] = int(day_month[1])
    if is_valid_date(day_month):
        return day_month[0]
    else:
        print("Error: Invalid date")


def is_valid_date(day_month):
    max_day_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 0 < day_month[0] <= max_day_per_month[day_month[1] + 1]:
        return True
    else:
        return False


def try_search_ship_by_name(ships, name):
    index_str = ""
    for i in range(len(name) - 1, 0, -1):
        try:
            int(name[i])
        except ValueError:
            break
        else:
            index_str += name[i]

    index = int(index_str[::-1])
    try:
        ships[index - 1]
    except IndexError:
        return search_ship_by_name(ships, name)
    else:
        if name == ships[index - 1].name:
            return ships[index - 1]
        else:
            return search_ship_by_name(ships, name)


def search_ship_by_name(ships, name):
    for i in range(len(ships)):
        if ships[i].name == name:
            return ships[i]


def closest_ships(ships):
    x = merge_sort_ships(deepcopy(ships), 0)
    y = merge_sort_ships(deepcopy(ships), 1)
    # TODO: matar ships y usar solo x
    ships = deepcopy(x)
    return closest_ships_r(ships, x, y)


def closest_ships_r(p, x, y):
    if len(p) <= 3:
        return closest_brute_force(p)

    j = 0
    p1 = Array(len(p) // 2, Ship())
    p2 = Array(len(p) - len(p) // 2, Ship())
    for i in range(len(p)):
        if i < len(p) // 2:
            p1[i] = p[i]
        else:
            p2[j] = p[i]
            j += 1

    xt = divide_coord(p1, p2, x)
    yt = divide_coord(p1, p2, y)
    dl = closest_ships_r(p1, xt[0], yt[0])
    dr = closest_ships_r(p2, xt[1], yt[1])
    d = min(dl, dr)
    
    # Armamos la "ventana"
    # TODO: Refactorear? No usar listas?
    strip_x = LinkedList()
    strip_y = LinkedList()
    middle_point = x[len(p) // 2]
    strip_x_length = 0
    strip_y_length = 0

    for i in range(len(p)):
        if abs(x[i].actual_position[0] - middle_point.actual_position[0]) < d:
            add(strip_x, x[i])
            strip_x_length += 1
        if abs(y[i].actual_position[0] - middle_point.actual_position[0]) < d:
            add(strip_y, y[i])
            strip_y_length += 1

    strip_x = list_to_array(strip_x, strip_x_length)
    strip_y = list_to_array(strip_y, strip_y_length)

    strip_x = merge_sort_ships(strip_x, 1)
    # Si alguno de los dos es None, nos quedamos con la menor distancia fuera de la "ventana"
    if strip_x is not None:
        min_a = min(d, strip_closest(strip_x, d))
    else:
        min_a = d

    if strip_y is not None:
        min_b = min(d, strip_closest(strip_y, d))
    else:
        min_b = d
    return min(min_a, min_b)


# Busca la mínima distancia dentro de nuestra "ventana"
def strip_closest(strip, d):
    min_val = d
    # Busca distancia con otros 6 barcos
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j].actual_position[1] -
                            strip[i].actual_position[1]) < min_val:
            min_val = distance(strip[i], strip[j])
            j += 1
    return min_val


# Divide el array de coordenadas en dos arrays según si pertenecen a p1 o a p2
def divide_coord(p1, p2, coord):
    i_l = i_r = 0
    coord_l = Array(len(p1), Ship())
    coord_r = Array(len(p2), Ship())
    for i in range(len(coord)):
        if search_ship_in_array(p1, coord[i]):
            coord_l[i_l] = coord[i]
            i_l += 1
        else:
            coord_r[i_r] = coord[i]
            i_r += 1
    return coord_l, coord_r


def search_ship_in_array(array, element):
    for i in range(len(array)):
        if are_equal_ships(array[i], element):
            return True
    return False


def closest_brute_force(ships):
    d = math.inf
    for i in range(len(ships)):
        for j in range(i + 1, len(ships)):
            current_d = distance(ships[i], ships[j])
            if current_d < d:
                d = current_d
    return d


def distance(b1, b2):
    x = pow(b1.actual_position[0] - b2.actual_position[0], 2)
    y = pow(b1.actual_position[1] - b2.actual_position[1], 2)
    return math.sqrt(x + y)

def merge_sort_ships(ships, coord):
    if ships is None:
        return
    ships_1 = Array(len(ships) // 2, Ship())
    ships_2 = Array(len(ships) - len(ships) // 2, Ship())
    j = 0

    if len(ships) > 1:
        for i in range(len(ships)):
            if i < len(ships) // 2:
                ships_1[i] = ships[i]
            else:
                ships_2[j] = ships[i]
                j += 1

        merge_sort_ships(ships_1, coord)
        merge_sort_ships(ships_2, coord)
        i = j = k = 0

        while i < len(ships_1) and j < len(ships_2):
            if ships_1[i].actual_position[coord] < ships_2[j].actual_position[coord]:
                ships[k] = ships_1[i]
                i += 1
            else:
                ships[k] = ships_2[j]
                j += 1
            k += 1

        # Chequeamos que no falte ningún elemento
        while i < len(ships_1):
            ships[k] = ships_1[i]
            i += 1
            k += 1

        while j < len(ships_2):
            ships[k] = ships_2[j]
            j += 1
            k += 1
    return ships


def search_collision_month(init_day,final_day,ships):
    for i in range(init_day,final_day):
        collision_list = search_collision(ships)
        if collision_list.head is not None:
            print("Collision detected in day ", i)
            print("Ships involved: ")
            print_list_ships(collision_list)
        update_ships_position(ships,i+1,init_day)

def print_list_ships(L):
    if L is None:
        print("List is None")
        return
    current = L.head
    currentPos = 0

    while current != None:
        if currentPos != 0: print(end=" -> ")
        print("(", current.value[0].name, " - ", current.value[1].name,")", end="")
        current = current.nextNode
        currentPos += 1
    print()
    return currentPos

def update_ships_position(ships,actual_day,init_day):
    for i in range(len(ships)):
        ships[i].update_position(actual_day,init_day)





def search_collision(ships):
    x = merge_sort_ships(deepcopy(ships), 0)
    y = merge_sort_ships(deepcopy(ships), 1)
    # TODO: matar ships y usar solo x
    ships = deepcopy(x)
    return search_collision_r(ships, x, y)


def search_collision_r(p, x, y):
    if len(p) <= 3:
        return collision_brute_force(p)

    j = 0
    p1 = Array(len(p) // 2, Ship())
    p2 = Array(len(p) - len(p) // 2, Ship())
    for i in range(len(p)):
        if i < len(p) // 2:
            p1[i] = p[i]
        else:
            p2[j] = p[i]
            j += 1

    xt = divide_coord(p1, p2, x)
    yt = divide_coord(p1, p2, y)
    dl = search_collision_r(p1, xt[0], yt[0])
    dr = search_collision_r(p2, xt[1], yt[1])
    collision_list = concat_list(dl,dr)
    d = math.sqrt(2)

    # Armamos la "ventana"
    # TODO: Refactorear? No usar listas?
    strip_x = LinkedList()
    strip_y = LinkedList()
    middle_point = x[len(p) // 2]
    strip_x_length = 0
    strip_y_length = 0
    #Agrega de forma ordenada los puntos dentro de la ventana, dentro de listas ordenadas por x y por y.
    for i in range(len(p)):
        if abs(x[i].actual_position[0] - middle_point.actual_position[0]) < d:
            add(strip_x, x[i])
            strip_x_length += 1
        if abs(y[i].actual_position[0] - middle_point.actual_position[0]) < d:
            add(strip_y, y[i])
            strip_y_length += 1

    strip_x = list_to_array(strip_x, strip_x_length)
    strip_y = list_to_array(strip_y, strip_y_length)

    #Ordena por y strip_x
    strip_x = merge_sort_ships(strip_x, 1)

    strip_x_list = strip_collision(strip_x, d)
    collision_list=concat_list(collision_list,strip_x_list)

    strip_y_list = strip_collision(strip_y, d)
    collision_list = concat_list(collision_list, strip_y_list)
    return collision_list

def strip_collision(strip,d):
    collision_list=LinkedList()
    # Busca distancia con otros 6 barcos
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j].actual_position[1] -
                            strip[i].actual_position[1]) < d:
            add(collision_list,[strip[j],strip[i]])
            j += 1
    return collision_list

def collision_brute_force(ships):
    collision_ships=LinkedList()
    d = math.inf
    for i in range(len(ships)):
        for j in range(i + 1, len(ships)):
            current_d = distance(ships[i], ships[j])
            if current_d < math.sqrt(2):
                d = add(collision_ships,[ships[i],ships[j]])
    return collision_ships
import math
from ship import *
from Algo1.algo1 import Array
from Algo1.mylinkedlist import LinkedList, add, list_to_array


class ShipDistance:
    distance = None
    ship1: None
    ship2: None


def closest_ships(ships, actual_day, initial_day):
    update_ships_position(ships, actual_day, initial_day)
    x = merge_sort_ships(deepcopy(ships), 0)
    y = merge_sort_ships(deepcopy(ships), 1)
    # TODO: matar ships y usar solo x
    ships = deepcopy(x)
    return closest_ships_r(ships, x, y)


def update_ships_position(ships, actual_day, initial_day):
    for i in range(len(ships)):
        ships[i].update_position_in_day(actual_day, initial_day)


def closest_ships_r(ships, ships_x, ships_y):
    if len(ships) <= 3:
        return closest_brute_force(ships)

    j = 0
    ships1 = Array(len(ships) // 2, Ship())
    ships2 = Array(len(ships) - len(ships) // 2, Ship())
    for i in range(len(ships)):
        if i < len(ships) // 2:
            ships1[i] = ships[i]
        else:
            ships2[j] = ships[i]
            j += 1

    ships_xt = divide_coord(ships1, ships2, ships_x)
    ships_yt = divide_coord(ships1, ships2, ships_y)
    ships_dl = closest_ships_r(ships1, ships_xt[0], ships_yt[0])
    ships_dr = closest_ships_r(ships2, ships_xt[1], ships_yt[1])
    ships_d = min_ships_distance(ships_dl, ships_dr)

    # Armamos la "ventana"
    strip_x = LinkedList()
    strip_y = LinkedList()
    middle_point = ships_x[len(ships) // 2]
    strip_x_length = 0
    strip_y_length = 0

    # Agrega los puntos dentro de la ventana en listas ordenadas por x y por y.
    for i in range(len(ships)):
        if abs(ships_x[i].actual_position[0] - middle_point.actual_position[0]) < ships_d.distance:
            add(strip_x, ships_x[i])
            strip_x_length += 1
        if abs(ships_y[i].actual_position[0] - middle_point.actual_position[0]) < ships_d.distance:
            add(strip_y, ships_y[i])
            strip_y_length += 1

    strip_x = list_to_array(strip_x, strip_x_length)
    strip_y = list_to_array(strip_y, strip_y_length)

    strip_x = merge_sort_ships(strip_x, 1)
    # Si alguno de los dos es None, nos quedamos con la menor distancia fuera de la "ventana"
    if strip_x is not None:
        min_a = min_ships_distance(ships_d, strip_closest(strip_x, ships_d.distance))
    else:
        min_a = ships_d

    if strip_y is not None:
        min_b = min_ships_distance(ships_d, strip_closest(strip_y, ships_d.distance))
    else:
        min_b = ships_d
    return min_ships_distance(min_a, min_b)


def min_ships_distance(ship_d1, ship_d2):
    if ship_d1.distance <= ship_d2.distance:
        return ship_d1
    else:
        return ship_d2


# Busca la mínima distancia dentro de nuestra "ventana"
def strip_closest(strip, d):
    ships_d = ShipDistance()
    ships_d.distance = d
    # Busca distancia con otros 6 barcos
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (abs(strip[j].actual_position[1] -
                                      strip[i].actual_position[1])) < ships_d.distance:
            ships_d.distance = distance(strip[i], strip[j])
            ships_d.ship1 = strip[i]
            ships_d.ship2 = strip[j]
            j += 1
    return ships_d


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
    ships_d = ShipDistance()
    ships_d.distance = math.inf
    for i in range(len(ships)):
        for j in range(i + 1, len(ships)):
            current_d = distance(ships[i], ships[j])
            if current_d < ships_d.distance:
                ships_d.distance = current_d
                ships_d.ship1 = ships[i]
                ships_d.ship2 = ships[j]
    return ships_d


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

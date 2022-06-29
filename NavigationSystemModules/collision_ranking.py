import math
from ship import *
from Algo1.algo1 import Array
from Algo1.mylinkedlist import LinkedList, add, list_to_array
from NavigationSystemModules.closer import ShipDistance, update_ships_position, min_ships_distance, divide_coord, \
    distance, merge_sort_ships


def make_collision_ranking(ships, actual_day, initial_day):
    update_ships_position(ships, actual_day, initial_day)
    x = merge_sort_ships(deepcopy(ships), 0)
    y = merge_sort_ships(deepcopy(ships), 1)
    ships = deepcopy(x)
    ranking = Array(10, Ship())
    return ranking_ships_r(ships, x, y, ranking)


def ranking_ships_r(ships, ships_x, ships_y, ranking):
    if len(ships) <= 3:
        return ranking_brute_force(ships, ranking)

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
    ships_dl = ranking_ships_r(ships1, ships_xt[0], ships_yt[0], ranking)
    ships_dr = ranking_ships_r(ships2, ships_xt[1], ships_yt[1], ranking)
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
    ranking_strip_closest(strip_x, ships_d.distance, ranking)
    ranking_strip_closest(strip_y, ships_d.distance, ranking)
    '''# Si alguno de los dos es None, nos quedamos con la menor distancia fuera de la "ventana"
    if strip_x is not None:
        min_a = min_ships_distance(ships_d, ranking_strip_closest(strip_x, ships_d.distance))
    else:
        min_a = ships_d

    if strip_y is not None:
        min_b = min_ships_distance(ships_d, ranking_strip_closest(strip_y, ships_d.distance))
    else:
        min_b = ships_d
    return min_ships_distance(min_a, min_b)'''


# Busca la mínima distancia dentro de nuestra "ventana"
def ranking_strip_closest(strip, d, ranking):
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
            add_ships_distance_to_ranking(ranking, ships_d)
            j += 1
    return ships_d


def ranking_brute_force(ships, ranking):
    ships_d = ShipDistance()
    current_d = ShipDistance()
    ships_d.distance = math.inf
    for i in range(len(ships)):
        for j in range(i + 1, len(ships)):
            current_d.distance = distance(ships[i], ships[j])
            current_d.ship1 = ships[i]
            current_d.ship2 = ships[j]
            add_ships_distance_to_ranking(ranking, current_d)

            if current_d.distance < ships_d.distance:
                ships_d.distance = current_d
                ships_d.ship1 = ships[i]
                ships_d.ship2 = ships[j]
    return ships_d


def add_ships_distance_to_ranking(ranking, ships_distance):
    there_are_nones = False
    for i in range(len(ranking)):
        if ranking[i] is None:
            there_are_nones = True
            ranking[i] = ships_distance
            merge_sort_ships_distance(ranking)

    if not there_are_nones:
        if ships_distance < ranking[9]:
            ranking[9] = ships_distance
            merge_sort_ships_distance(ranking)


def merge_sort_ships_distance(ships_distances):
    if ships_distances is None:
        return
    ships_1 = Array(len(ships_distances) // 2, Ship())
    ships_2 = Array(len(ships_distances) - len(ships_distances) // 2, Ship())
    j = 0

    if len(ships_distances) > 1:
        for i in range(len(ships_distances)):
            if i < len(ships_distances) // 2:
                ships_1[i] = ships_distances[i]
            else:
                ships_2[j] = ships_distances[i]
                j += 1

        merge_sort_ships_distance(ships_1)
        merge_sort_ships_distance(ships_2)
        i = j = k = 0

        while i < len(ships_1) and j < len(ships_2):
            if ships_1[i].distance < ships_2[j].distance:
                ships_distances[k] = ships_1[i]
                i += 1
            else:
                ships_distances[k] = ships_2[j]
                j += 1
            k += 1

        # Chequeamos que no falte ningún elemento
        while i < len(ships_1):
            ships_distances[k] = ships_1[i]
            i += 1
            k += 1

        while j < len(ships_2):
            ships_distances[k] = ships_2[j]
            j += 1
            k += 1
    return ships_distances

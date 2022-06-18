import math
import sys
from ship import *
from algo1 import Array
from mylinkedlist import LinkedList, add, list_to_array


def create_index(path):
    with open(path) as f:
        lines = f.readlines()

    ships = Array(len(lines) - 1, Ship())
    for i in range(0, len(ships)):
        index = 0
        data = ["", "", "", ""]
        # TODO: usar isNullOrEmpty
        if lines[i+1] != "\n" and lines[i+1] != "":
            for j in range(len(lines[i + 1])):
                if lines[i + 1][j] != " " and lines[i + 1][j] != "\n":
                    data[index] += lines[i + 1][j]
                else:
                    index += 1
            ships[i] = Ship(data[0], [int(data[1]), int(data[2])], data[3])

    return ships


def search(ships, date, name):
    day = get_day(date)
    if day is not None:
        ship = try_search_ship_by_name(ships, name)
        ship.update_position(day)
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
        print("Invalid date")


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
    x = merge_sort_ships(ships, Array(len(ships), Ship()), 0)
    y = merge_sort_ships(ships, Array(len(ships), Ship()), 1)
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
    print(strip_x, strip_y)
    strip_x = merge_sort_ships(strip_x, Array(len(strip_x), Ship()), 1)
    min_a = min(d, strip_closest(strip_x, len(strip_x), d))
    min_b = min(d, strip_closest(strip_y, len(strip_y), d))

    return min(min_a, min_b)


def strip_closest(strip, size, d):
    min_val = d

    # Busca distancia con otros 6 barcos
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].actual_position[1] -
                            strip[i].actual_position[1]) < min_val:
            min_val = distance(strip[i], strip[j])
            j += 1

    return min_val


def divide_coord(p1, p2, coord):
    i_l = i_r = 0
    coord_l = p1
    coord_r = p2
    for i in range(len(coord)):
        if search_array(p1, coord[i]):
            coord_l[i_l] = coord[i]
            i_l += 1
        else:
            coord_r[i_r] = coord[i]
            i_r += 1
    return coord_l, coord_r


def search_array(array, element):
    for i in range(len(array)):
        if array[i] == element:
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


# TODO: Arreglarlo. No está funcionando por el ord_ships
def merge_sort_ships(ships, ord_ships, coord):
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

        merge_sort_ships(ships_1, ord_ships, coord)
        merge_sort_ships(ships_2, ord_ships, coord)
        i = j = k = 0

        while i < len(ships_1) and j < len(ships_2):
            if ships_1[i].actual_position[coord] < ships_2[j].actual_position[coord]:
                ord_ships[k] = ships_1[i]
                i += 1
            else:
                ord_ships[k] = ships_2[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(ships_1):
            ord_ships[k] = ships_1[i]
            i += 1
            k += 1

        while j < len(ships_2):
            ord_ships[k] = ships_2[j]
            j += 1
            k += 1
    return ord_ships

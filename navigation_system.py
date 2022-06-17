import math
import sys
from ship import *
from algo1 import Array


def create_index(path):
    with open(path) as f:
        lines = f.readlines()

    ships = Array(len(lines) - 1, Ship())
    for i in range(0, len(ships)):
        index = 0
        data = ["", "", "", ""]
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
    return closest_ships_r(merge_sort_ships(ships, 0), merge_sort_ships(ships, 0), merge_sort_ships(ships, 1))


def closest_ships_r(p, x, y):
    if len(p) <= 3:
        return closest_brute_force(p)

    j = 0
    p1=Array(len(p)//2,Ship())
    p2=Array(len(p)-len(p)//2,Ship())
    for i in range(len(p)):
        if i < len(p) // 2:
            p1[i] = p[i]
        else:
            p2[j] = p[i]
            j += 1

    xt = divide_coord(p1,p2,x)
    yt = divide_coord(p1,p2,y)
    dl = closest_ships_r(p1, xt[0], yt[0])
    dr = closest_ships_r(p2, xt[1], yt[1])
    return min(dl,dr)

def divide_coord(p1,p2,coord):
    i_l = i_r = 0
    coord_l=p1
    coord_r = p2
    for i in range(len(coord)):
        if search_array(p1,coord[i]):
            coord_l[i_l] = coord[i]
            i_l += 1
        else:
            coord_r[i_r] = coord[i]
            i_r += 1
    return coord_l,coord_r

def search_array(array,element):
    for i in range(len(array)):
        if array[i]==element:
            return True

    return False

def closest_brute_force(ships):
    d = math.inf
    for i in range(len(ships)):
        for j in range(i+1, len(ships)):
            x = pow(ships[j].actual_position[0]-ships[i].actual_position[0], 2)
            y = pow(ships[j].actual_position[1]-ships[i].actual_position[1], 2)
            current_d = math.sqrt(x+y)
            if current_d < d:
                d = current_d

    return d

#TODO: Arreglarlo.
def merge_sort_ships(ships, coord):
    s = ships
    ships_1 = Array(len(s) // 2, Ship())
    ships_2 = Array(len(s) - len(s) // 2, Ship())
    j = 0

    if len(s) > 1:
        for i in range(len(s)):
            if i < len(s) // 2:
                ships_1[i] = s[i]
            else:
                ships_2[j] = s[i]
                j += 1

        merge_sort_ships(ships_1, coord)
        merge_sort_ships(ships_2, coord)
        i = j = k = 0

        while i < len(ships_1) and j < len(ships_2):
            if ships_1[i].actual_position[coord] < ships_2[j].actual_position[coord]:
                s[k] = ships_1[i]
                i += 1
            else:
                s[k] = ships_2[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(ships_1):
            s[k] = ships_1[i]
            i += 1
            k += 1

        while j < len(ships_2):
            s[k] = ships_2[j]
            j += 1
            k += 1
    return s

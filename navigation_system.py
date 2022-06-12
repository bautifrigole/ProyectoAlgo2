import sys
from ship import *
from algo1 import Array


def create_index():
    with open('ship_report.txt') as f:
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
        ships[i] = Ship(data[0], (int(data[1]), int(data[2])), data[3])


def search(ships, date, name):
    # TODO: get_day(date)
    ship = try_search_ship_by_name(ships, name)
    ship.update_position(date)
    return ship.actual_x, ship.actual_y


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
            return ships[index-1]
        else:
            return search_ship_by_name(ships, name)


def search_ship_by_name(ships, name):
    for i in range(len(ships)):
        if ships[i].name == name:
            return ships[i]

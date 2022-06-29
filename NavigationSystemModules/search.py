def search(ships, day_month, name, initial_day):
    actual_day = day_month[0]
    if actual_day is not None:
        ship = try_search_ship_by_name(ships, name)

        if ship is not None:
            ship.update_position_in_day(actual_day, initial_day)
            return ship.actual_position


def try_search_ship_by_name(ships, name):
    index_str = ""
    for i in range(len(name) - 1, -1, -1):
        try:
            int(name[i])
        except ValueError:
            break
        else:
            index_str += name[i]

    try:
        index = int(reverse_str(index_str))
    except ValueError:
        return search_ship_by_name(ships, name)

    try:
        ships[index - 1]
    except IndexError:
        return search_ship_by_name(ships, name)
    else:
        if name == ships[index - 1].name:
            return ships[index - 1]
        else:
            return search_ship_by_name(ships, name)


def reverse_str(string):
    reverse = ""
    for i in range(len(string) - 1, -1, -1):
        reverse += string[i]
    return reverse


def search_ship_by_name(ships, name):
    for i in range(len(ships)):
        if ships[i].name == name:
            return ships[i]

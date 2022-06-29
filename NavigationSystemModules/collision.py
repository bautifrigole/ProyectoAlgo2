import math
from ship import *
from Algo1.algo1 import Array
from Algo1.mylinkedlist import LinkedList, add, list_to_array, concat_list
from NavigationSystemModules.closer import merge_sort_ships, divide_coord, distance


def search_collision_month(init_day, final_day, ships):
    collision_detected = False
    for i in range(init_day, final_day + 1):
        collision_list = search_collision(ships)
        if collision_list is not None and collision_list.head is not None:
            collision_detected = True
            print("Collision detected in day ", i)
            print("Ships involved: ")
            print_list_ships(collision_list)
            print()
        update_ships_position(ships)
    if not collision_detected:
        print(collision_detected)


def print_list_ships(L):
    if L is None:
        print("List is None")
        return
    current = L.head
    current_pos = 0

    while current is not None:
        if current_pos != 0: print(end=" - ")
        print("(", current.value[0].name, "-", current.value[1].name, ")", end="")
        current = current.nextNode
        current_pos += 1
    print()
    return current_pos


def update_ships_position(ships):
    for i in range(len(ships)):
        ships[i].update_position_next_day()


def search_collision(ships):
    x = merge_sort_ships(deepcopy(ships), 0)
    y = merge_sort_ships(deepcopy(ships), 1)
    # TODO: matar ships y usar solo x
    ships = deepcopy(x)
    return search_collision_r(ships, x, y)


def search_collision_r(ships, ships_x, ships_y):
    if len(ships) <= 3:
        return collision_brute_force(ships)

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
    dl = search_collision_r(ships1, ships_xt[0], ships_yt[0])
    dr = search_collision_r(ships2, ships_xt[1], ships_yt[1])
    collision_list = concat_list(dl, dr)

    # Definimos d igual a raíz de 2 ya que es el radio que queremos de nuestra ventana
    d = math.sqrt(2)

    # Armamos la "ventana"
    strip_x = LinkedList()
    strip_y = LinkedList()
    middle_point = ships_x[len(ships) // 2]
    strip_x_length = 0
    strip_y_length = 0

    # Agrega los puntos dentro de la ventana en listas ordenadas por x y por y.
    for i in range(len(ships)):
        if abs(ships_x[i].actual_position[0] - middle_point.actual_position[0]) <= d:
            add(strip_x, ships_x[i])
            strip_x_length += 1
        if abs(ships_y[i].actual_position[0] - middle_point.actual_position[0]) <= d:
            add(strip_y, ships_y[i])
            strip_y_length += 1

    strip_x = list_to_array(strip_x, strip_x_length)
    strip_y = list_to_array(strip_y, strip_y_length)

    # Ordena por y strip_x
    strip_x = merge_sort_ships(strip_x, 1)

    strip_collision(strip_x, collision_list, d)
    strip_collision(strip_y, collision_list, d)
    return collision_list


# Busca en la "ventana" los barcos que están a distancia menor o igual a raíz de 2
def strip_collision(strip, collision_list, d):
    # Busca distancia con otros 6 barcos
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (abs(strip[j].actual_position[1] -
                                      strip[i].actual_position[1])) <= d:
            if not search_pair_of_ships_in_list(collision_list, strip[j], strip[i]):
                add(collision_list, [strip[j], strip[i]])
            j += 1
    return collision_list


def collision_brute_force(ships):
    collision_ships = LinkedList()
    for i in range(len(ships)):
        for j in range(i + 1, len(ships)):
            current_d = distance(ships[i], ships[j])
            if current_d <= math.sqrt(2):
                add(collision_ships, [ships[i], ships[j]])
    return collision_ships


def search_pair_of_ships_in_list(list, ship1, ship2):
    if list is not None:
        node = list.head
        while node is not None:
            if (are_equal_ships(node.value[0], ship1) and are_equal_ships(node.value[1], ship2)) or \
                    (are_equal_ships(node.value[0], ship2) and are_equal_ships(node.value[1], ship1)):
                return True
            node = node.nextNode
        return False

import pickle
import sys
from NavigationSystemModules.date_management import get_last_day, get_day_month
from NavigationSystemModules.creation import create_index
from NavigationSystemModules.search import search
from NavigationSystemModules.closer import closest_ships
from NavigationSystemModules.collision import search_collision_month

SHIPS_ID = 'ships.pkl'
DATE_ID = 'date.pkl'


def serialize_ships(path):
    with open(path) as f:
        date = f.readline()

    with open(DATE_ID, 'wb') as pickle_file:
        pickle.dump(get_day_month(date), pickle_file)

    ships = create_index(path)
    with open(SHIPS_ID, 'wb') as pickle_file:
        pickle.dump(ships, pickle_file)
    print(len(ships), "ships loaded successfully")


if sys.argv[1] == "-create":
    serialize_ships(sys.argv[2])


def search_wrapper(date, name):
    with open(SHIPS_ID, 'rb') as pickle_file:
        ships = pickle.load(pickle_file)

    with open(DATE_ID, 'rb') as pickle_file:
        initial_date = pickle.load(pickle_file)
    day_month = get_day_month(date)
    if day_month is not None:
        if day_month[2] != initial_date[2]:
            print("Error! You are trying to search for boats in another year than the one given in the file")
            return
        if day_month[1] != initial_date[1]:
            print("Error! You are trying to search for boats in another month than the one given in the file")
            return
        position = search(ships, day_month, name, initial_date[0])
        if position is not None:
            print(f"Position of '{name}' in {date}: {position}")
        else:
            print(f"Ship with name '{name}' not found")


if sys.argv[1] == "-search":
    search_wrapper(sys.argv[2], sys.argv[3])


def closest_wrapper(date):
    with open(SHIPS_ID, 'rb') as pickle_file:
        ships = pickle.load(pickle_file)

    with open(DATE_ID, 'rb') as pickle_file:
        initial_date = pickle.load(pickle_file)
    actual_date = get_day_month(date)
    if actual_date is not None:
        if actual_date[2] != initial_date[2]:
            print("Error! You are trying to search for boats in another year than the one given in the file")
            return
        if actual_date[1] != initial_date[1]:
            print("Error! You are trying to search for boats in another month than the one given in the file")
            return
        ships_d = closest_ships(ships, actual_date[0], initial_date[0])
        print(f"'{ships_d.ship1.name}' and '{ships_d.ship2.name}' with distance: '{ships_d.distance}'")


if sys.argv[1] == "-closer":
    closest_wrapper(sys.argv[2])


def collision_wrapper():
    with open(SHIPS_ID, 'rb') as pickle_file:
        ships = pickle.load(pickle_file)

    with open(DATE_ID, 'rb') as pickle_file:
        initial_date = pickle.load(pickle_file)

    search_collision_month(initial_date[0], get_last_day(initial_date[1]), ships)


if sys.argv[1] == "-collision":
    collision_wrapper()

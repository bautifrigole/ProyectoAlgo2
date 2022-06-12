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
        ships[i] = Ship(data[0], (int(data[1]), int(data[2])), data[3])

    return ships


def search(ships, date, name):
    day=get_day(date)
    if day!=None:
        ship = try_search_ship_by_name(ships, name)
        ship.update_position(day)
        return ship.actual_x, ship.actual_y
    

def get_day(date):
    day_month=["",""]
    index=0
    flag1=False
    for i in range(len(date)):
        if date[i]!="-":
            day_month[index]+=date[i]
        else:
            index+=1
            if index==2:
                break
    
    day_month[0]=int(day_month[0])
    day_month[1]=int(day_month[1])
    if is_valid_date(day_month):
        return day_month[0]
    else:
        print ("Invalid date")
        

def is_valid_date(day_month):
    maxday_per_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if day_month[0]>0 and day_month[0]<=maxday_per_month[day_month[1]+1]:
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
            return ships[index-1]
        else:
            return search_ship_by_name(ships, name)


def search_ship_by_name(ships, name):
    for i in range(len(ships)):
        if ships[i].name == name:
            return ships[i]

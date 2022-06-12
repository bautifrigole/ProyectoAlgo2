from ship import *
from algo1 import Array
from navigation_system import *

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

print(search(ships, 4, "barco4"))

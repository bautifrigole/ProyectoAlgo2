import pickle
from ship import *

with open('ship_report.txt') as f:
    lines = f.readlines()

ships = [lines[i] for i in range(1, len(lines))]
#for i in range(1, len(lines)):
    # ir recorriendo el string hasta encontrar un espacio
    # name, posX, posY, direction
    #ships[i] = Ship(name, initial_position, direction)

#with open('ships', 'bw') as f:
#    pickle.dump()

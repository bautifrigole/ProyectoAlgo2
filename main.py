from ship import *
from algo1 import Array
from navigation_system import *
import random

ships = Array(random.randint(5, 15), Ship())
directions = ["N", "S", "E", "W", "NE", "SE", "NW", "SW"]

for i in range(0, len(ships)):
    ships[i] = Ship("barco"+str(i+1), [random.randint(-5, 5), random.randint(-5, 5)], directions[random.randint(0, 7)])


#ships = create_index('ship_report.txt')
#print(search(ships, "30-05-2022", "barco4"))

search_collision_month(1, 31, ships)
print(ships)
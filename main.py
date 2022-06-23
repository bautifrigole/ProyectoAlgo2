from ship import *
from algo1 import Array
from navigation_system import *

ships = create_index('ship_report.txt')
#print(search(ships, "30-05-2022", "barco4"))
print(search_collision_month(1,31,ships))

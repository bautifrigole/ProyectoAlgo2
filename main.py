from ship import *
from algo1 import Array
from navigation_system import *

ships = create_index('ship_report.txt')
print(ships)
#print(search(ships, "30-05-2022", "barco4"))
merge_sort_ships(ships, 1)
print(ships)

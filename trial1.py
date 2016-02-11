"""
First trial
"""

from heapq import nlargest, nsmallest
from pprint import pprint
import load
# OPS === L:LOAD U:UNLOAD D:DELIVERY

sim, items, warehouse, orders = load.read_input('datos/busy_day.in')
pprint(items)

drones = [{'id':i, 'max_load': sim['max_load'], 'wheight': 0} for i in xrange(sim['drones'])]

def load(drone_id, warehouse_id, item_type_id, item_quantity):
    """
    """
    drone_wheight = drones[drone_id]['wheight']
    drone_max_load = drones[drone_id]['max_load']
    items_weight = int(items[item_type_id]['wheight'] * item_quantity)
    if drone_wheight + items_weight > drone_max_load:
        return False
    return '%i L %i %i %i' %(drone_id, warehouse_id, item_type_id, item_quantity)

def delivery(drone_id, order_id, item_type_id, item_quantity):
    """
    """
    return '%i D %i %i %i' %(drone_id, order_id, item_type_id, item_quantity)

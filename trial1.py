"""
First trial
"""

from heapq import nlargest, nsmallest
from pprint import pprint
import load
# OPS === L:LOAD U:UNLOAD D:DELIVERY

sim, items, warehouses, orders = load.read_input('datos/redundancy.in')
drones = [{'id':i, 'max_load': sim['max_load'], 'weight': 0} for i in xrange(sim['drones'])]

#### check stock

### check weight

def find_item(item_id):
    """
    """
    for i,w in enumerate(warehouses):
        if w['stock'][item_id] == 0:
            continue
        return i

def load(drone_id, warehouse_id, item_type_id, item_quantity):
    """
    """
    print warehouse_id
    item_weight = int(items[item_type_id]['weight'])
    drone_max_load = drones[drone_id]['max_load']
    drone_weight = drones[drone_id]['weight']
    quantity_items_take = 0
    for i in xrange(item_quantity):
        if warehouses[warehouse_id]['stock'][item_type_id] + item_weight > drone_max_load:
            break
        if warehouses[warehouse_id]['stock'][item_type_id] == 0:
            break
        # update drone weight
        drones[drone_id]['weight'] += item_weight
        quantity_items_take +=1
        # update item stock
        items[item_type_id]['stock'][warehouse_id] -= 1
        warehouses[warehouse_id]['stock'][item_type_id] -= 1
    print warehouse_id
    return quantity_items_take, '%i L %i %i %i' %(drone_id, warehouse_id, item_type_id, quantity_items_take)

def delivery(drone_id, order_id, item_type_id, item_quantity):
    """
    """
    drones[drone_id]['weight'] = 0
    return '%i D %i %i %i' %(drone_id, order_id, item_type_id, item_quantity)

def start():
    list_commands = []
    drone = 0
    max_drone = sim['drones']
    for order_id,order in enumerate(orders):
        print('order %i' % order_id)
        for item_type_id, quantity in order["items"].iteritems():
            print('item %i' % item_type_id)
            while(True):
                print('quantity is: %i' % quantity)
                warehouse_id = find_item(item_type_id)
                if warehouse_id is None:
                    break
                items_take, command = load(drone, warehouse_id, item_type_id, quantity)
                list_commands.append(command)
                list_commands.append(delivery(drone, order_id, item_type_id, items_take))
                quantity -= items_take
                if items_take == 0:
                    break
            drone = (drone + 1) % max_drone
    return list_commands

commands = start()
with open('redun.in', 'w') as f:
    f.write(str(len(commands)) + '\n')
    for c in commands:
        f.write(c + '\n')

from heapq import nlargest, nsmallest

warehouses = []
products = []


def calculate_weight(item):
    # for p_id, amount in item["items"].iteritems():
    #     print p_id,amount
    #     print product[p_id]
    #
    return item["weight"]

def sort_orders(orders):

    return nsmallest(len(orders),orders,key=calculate_weight)

if __name__ == "__main__":
    import load
    sim, products, warehouses, orders = load.read_input('datos/busy_day.in')

    print
    orders = sort_orders(orders)
    print
    for o in orders:
        print o["weight"]

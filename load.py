
def read_input(filename):
    with open(filename) as f:
        sim_params = f.readline().split(" ")
        sim = {
            "rows":int(sim_params[0]),
            "cols":int(sim_params[1]),
            "drones":int(sim_params[2]),
            "deadline":int(sim_params[3]),
            "max_load":int(sim_params[4])
        }

        num_products = int(f.readline())

        products=[]
        pesos = f.readline().split(" ")
        for product in pesos:
            products.append({"weight":int(product),"stock":{}})

        if len(products) != num_products:
            print "!!!!!!!!!!!!!!!!!!!!"

        num_warehouses = int(f.readline())
        print num_warehouses
        warehouses = []
        warehouse_id =0
        for i in range(num_warehouses):
            pos = f.readline().split(" ")
            warehouse_stock =  f.readline().split(" ")
            warehouse = {
                "position" : {
                    "x": int(pos[1]),
                    "y": int(pos[0])
                },
                "stock":[]
            }
            prod_id=0
            for prod_stock in warehouse_stock:
                warehouse["stock"].append(int(prod_stock))
                products[prod_id]["stock"][warehouse_id] = int(prod_stock)
                prod_id += 1
            warehouses.append(warehouse)
            warehouse_id += 1

        num_orders = int(f.readline())
        orders =[]
        for i in range(num_orders):
            pos = f.readline().split(" ")
            order = {
                "position" : {
                    "x": int(pos[1]),
                    "y": int(pos[0])
                },
                "items": {},
                "weight": 0
            }
            num_items = int(f.readline())
            items =  f.readline().split(" ")
            for i in items:
                if int(i) not in order["items"]:
                    order["items"][int(i)]=0
                order["items"][int(i)] +=1
                order["weight"] += products[int(i)]["weight"]
            orders.append(order)
    return sim, products, warehouses, orders

if __name__ == '__main__':
    from pprint import pprint
    s,p,w,ord= read_input("datos/busy_day.in")
    pprint (ord[0])

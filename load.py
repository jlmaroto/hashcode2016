
def read_input(filename):
    with open(filename) as f:
        sim_params = f.read_line().split(" ")
        sim = {
            "rows":int(sim_params[0]),
            "cols":int(sim_params[1]),
            "drones":int(sim_params[2]),
            "deadline":int(sim_params[3]),
            "max_load":int(sim_params[4])
        }

        num_products = int(f.read_line())

        products=[]
        pesos = f.read_line().split(" ")
        for product in pesos:
            products.append({"peso":int(product),"stock":{}})


        if len(products) != num_products:
            print "!!!!!!!!!!!!!!!!!!!!"

        num_warehouses = int(f.read_line())
        warehouses = []
        warehouse_id =0
        for i in range(num_warehouses):
            pos = f.read_line().split(" ")
            warehouse_stock =  f.read_line().split(" ")
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

        num_orders = int(f.read_line())
        orders =[]
        for i in range(num_orders):
            pos = f.read_line().split(" ")
            order = {
                "position" : {
                    "x": int(pos[1]),
                    "y": int(pos[0])
                },
                "items": {}
            }
            num_items = int(f.read_line())
            items =  f.read_line().split(" ")
            for i in items:
                if int(i) not in order["items"]:
                    order["items"][int(i)]=0
                order["items"][int(i)] +=1
            orders.append(order)

    return sim, products, warehouse, orders




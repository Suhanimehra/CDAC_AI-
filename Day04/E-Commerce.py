catalog = {
        "P01": {"price": 100.0, "stock": 5},
        "P02": {"price": 50.0, "stock": 2}
    }


class ProductNotFoundError(Exception):
    pass

class OutOfStockError(Exception):
    pass


def  process_order(catalog, order):
    total_price=0.0
    for product_id , requested_quantity in order.items(): 
        if product_id not in catalog:
            raise ProductNotFoundError() 


        available_stock = catalog[product_id]["stock"]

        if requested_quantity>available_stock:
            raise OutOfStockError()


        price=catalog[product_id]["price"]

        total_price+=(price*requested_quantity)

        catalog[product_id]["stock"] -= requested_quantity

    return total_price

a=process_order(catalog, {"P01": 2, "P02": 1})
print(a)
print(catalog)
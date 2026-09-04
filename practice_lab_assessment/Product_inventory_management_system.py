import re

#-------------------sample data---------------------
products = [
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10},
{"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50}
]
#----------------------------------------
id_counter=2

def menu():
    print('-'*50)
    print("Product Inventry Managment System")
    print("Menu: ")
    print(" 1. Add Product \n 2. View All Products \n 3. Search Product \n 4. Update Product \n 5. Delete Product \n 6. Exit")
    print('-'*50)
#--------------------------------------------------------------------------------------------------
def add_products():
    
    global id_counter
    try:
        name=input("Enter the name: ")
        if name=='':
            print("Invalid Input Name cannot be empty.")
            return
            
        category=input("Enter Category: ")
        if category=='':
            print("Invalid Input Name cannot be empty.")
            return
        
        price=float(input("Enter Price: "))
        if price<=0:
            print("Price cannot be negative/zero.")
            return
        
        quantity=int(input("Enter Qauntity: "))
        if quantity <0:
            print("Quantity cannot be negative/zero.")
            return
        
        products.append(dict(id = id_counter+1,name=name , category=category , price=price, quantity=quantity))
            
        id_counter +=1
    except:
        raise ValueError("Invalid Value. Enter a valid value.")
    
#--------------------------------------------------------------------------------------------------
def one_product(p):
    pid,name,category,price,quantity=p.values()
    
    print("----Product Details----")
    print(f"ID:         {pid}")
    print(f"Name:       {name}")
    print(f"Category:   {category}")
    print(f"Price:      {price}")
    print(f"Quantity:   {quantity}")
    print('-'*60)
#--------------------------------------------------------------------------------------------------
def many_product(products_list):
    print("----Product Details----")
    print('-'*60)
    
    print(f"{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}") 
    print('-'*60)
    
    for p in products_list:
        pid,name,category,price,quantity=p.values()
        print(f"{pid:^5}{name:<20}{category:<20}{price:>10.2f}{quantity:>5}")
       
    
    print('-'*60)
#--------------------------------------------------------------------------------------------------
def view_products():
    
    if len(products)==0:
        print("No products in the list")
        
    elif len(products)==1:
        one_product(products[0])
    else:
        many_product(products)       
#--------------------------------------------------------------------------------------------------
def search_produts():
    try:
        search_choice=int(input("Enter 1 for searching by product ID: \nEnter 2 for searching by name: "))
        if search_choice==1:
            pid=int(input("Enter the product id you want to search: "))
            search_product_id(pid)
            
        elif search_choice==2:
            search_name()

        else:
            ("Print Enter a valid choice.")
    except:
        print("Try with a valid integer.")

#--------------------------------------------------------------------------------------------------

def search_product_id(pid):

    result=[p for p in products if p['id']==pid]
    if not result:
        print(f"No product found for id {pid}")
        return None

    one_product(result[0])
    return result[0]

#--------------------------------------------------------------------------------------------------
def search_name():

    name = input("Enter the product name you want to  search")

    result=[p for p in products if p['name']==name]
    if not result:
        print(f"No product found for name {name}")
        return None

    if len(result)==1:
        one_product(result[0])

    else:
        many_product(result)
    
#--------------------------------------------------------------------------------------------------
def update_product():
    try:
        update_pid=int(input("Enter the Product id you want to update:" ))

        result=[p for p in products if p['id']==update_pid]

        if not result:
            print(f"No product found for name {update_pid}")
            return None

        
        else:

            name=input("Enter the update name: ")
            if name=='':
                print("Invalid Input Name cannot be empty.")
                return
            
            category=input("Enter the update category: ")
            if category=='':
                print("Invalid Input Name cannot be empty.")
                return
            price=float(input("Enter the update price: "))
            if price<=0:
                print("Price cannot be negative/zero.")
                return
            quantity=int(input("Enter the update quantity: "))
            if quantity <0:
                print("Quantity cannot be negative/zero.")
                return

            result[0]['name']=name
            result[0]['category']=category
            result[0]['price']=price
            result[0]['quantity']=quantity

            one_product(result[0])
    except:
        print("Enter a valid integer")
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def delete_product():
    try:
        pid_1=int(input("Enter the product id of product you want to delete: "))


        product=search_product_id(pid_1)

        if product is None:
            return

        else:
            delete_choice=input("Are you sure [y/n]: ")

            if delete_choice.lower()=='y':

                products.remove(product)
                print("Prodct Deleted Successfully")
            else:
                print("Product was not deleted.")

    except:
        print("Enter a Valid integer ")



#--------------------------------------------------------------------------------------------------
def main():
    while True:

        menu()
        menu_choice= int(input("Enter Your Choice: "))
        
        print('-'*50)

        match menu_choice:
            case 1:
                add_products()
            case 2:
                view_products()
            case 3:
                search_produts()
            case 4:
                update_product()
            case 5:
                delete_product()
            case 6:
                break
            case _:
                print("Invalid Choice.")



if __name__== '__main__':
    main()


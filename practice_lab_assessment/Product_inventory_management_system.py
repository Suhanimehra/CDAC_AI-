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
        
        price=int(input("Enter Price: "))
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
        print(f"{pid:^5}{name:<20}{category:<20}{price:>10}{quantity:>5}")
       
    
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
#--------------------------------------------------------------------------------------------------
def main():
    while True:

        menu()
        choice= int(input("Enter Your Choice: "))
        
        print('-'*50)

        match choice:
            case 1:
                add_products()
            case 2:
                view_products()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print("Invalid Choice.")



if __name__== '__main__':
    main()


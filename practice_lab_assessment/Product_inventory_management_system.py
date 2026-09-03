#-------------------sample data---------------------
products = [
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10},
{"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50}
]
#----------------------------------------
def menu():
    print('-'*50)
    print("Product Inventry Managment System")
    print("Menu: ")
    print(" 1. Add Product \n 2. View All Products \n 3. Search Product \n 4. Update Product \n 5. Delete Product \n 6. Exit")
    print('-'*50)
#--------------------------------------------------------------------------------------------------
def add_prduct():
    pass
#--------------------------------------------------------------------------------------------------
def main():
    while True:

        menu()
        choice= int(input("Enter Your Choice: "))

        match choice:
            case 1:
                add_prduct()
            case 2:
                pass
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


inventory = {"Python Basics": 10, "Learning AI": 5}

def manage_bookstore_inventory(inventory, action, book_title, quantity=0):

    if action.lower() not in ('sell','add','lookup'):
        print("Invalid Action")
        return

    if action.lower()=="add":

        if book_title in inventory:
            inventory[book_title] +=quantity

        else:
            inventory[book_title] = quantity


        return inventory

    if action.lower()=="sell":

        if book_title not in inventory:
            print(f"Error: Book {book_title} not found in inventory.")
            return inventory

        if inventory[book_title] < quantity:
            print(f"Error: Insufficient stock for {book_title}. Available:{inventory[book_title]}")
            return inventory
        else:
            inventory[book_title]-=quantity

            if inventory[book_title]==0: del inventory[book_title]   

            return inventory
    if action.lower()=="lookup":
        return inventory.get(book_title, 0)

m=manage_bookstore_inventory(inventory, "add", "Python Basics", 3)
y= manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)
z= manage_bookstore_inventory(inventory, "lookup", "Learning AI", 10)
# d= manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
# print(d)
print(z)
print(m)
print(y)
def nightclub():
    
    list1=["Guido", "Esha", "Rajan", "Kishori"]
    while True:
        
        guest=input("Enter user name: ")
        
        if guest=="exit":
            break
        
        if guest in list1:
            list1.remove(guest)
            
            list1.insert(0,guest)
            
            print(f"{guest} is moved to the first ")
            
            print(list1)
        
        
        else:
            print("Access denied. Not on the VIP list")
        
        
        
    
nightclub()
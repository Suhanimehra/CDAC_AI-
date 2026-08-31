def cargo(wagon):
    
    
    
    resource=input("enter the resource you want to count: ")
    
    count=wagon.count(resource)
    
    if count >0:
        
        print(f"{resource} is found in the wagon at index {wagon.index(resource)}.")
        
    else:
        print(f"{resource} is not in the wagon.")
    
    
wagon=["coal", "iron", "gold", "coal", "timber", "coal"]  
cargo(wagon)


def duplicate():
    
    str1=["apple", "banana", "apple", "orange", "banana", "banana"]
    
    str2=[]
    
    for item in str1:
        
        if item not in str2:
            str2.append(item)
        
    print(str2)
duplicate()
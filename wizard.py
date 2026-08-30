def magic():
    item=["staff","potion","spellbook"]
    
    new_item=input("Enter a new item to add to your inventory: ")
    
    item.append(new_item)
    item.pop(0)
    
    print("Portal transition activated! Ejected oldest item: staff Current items in the magic bag: ",item)
    
magic()
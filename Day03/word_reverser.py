def spy():
    sen=input("Enter the sentence: ")
    
    split_sen=sen.split(" ")
    
    
    reverse_sen = [word[::-1] for word in split_sen] # here word[::-1 reverse the individual word , we dont use reverse becuase it reverses the whole list not each word ]
    
    print(" " .join(reverse_sen))
    
spy()
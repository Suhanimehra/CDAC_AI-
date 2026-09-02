def main():

    text=input("Enter text: ")
    shift=int(input("Enter shift: "))
    

    # a= [chr(ord(c) + shift) for c in text] this way we get all the next shift charactersof alphabet 
    a= "".join(chr(ord(c)+shift) for c in text) # here we als joi them in one string using join function 

    print(a)

main()
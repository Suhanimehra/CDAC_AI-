class InvalidPhoneNumberError(Exception):
    pass

name=input("Enter name: ")
number=input("Enter Number: ")

phonebook={}

def check_name(name):
    
    if not name:
        raise ValueError("Contact name must be a non-empty alphabetic string.")
    if not name.strip():
        raise ValueError("Contact name must be a non-empty alphabetic string.")
    for char in name:
       
        if not (char.isalpha() or char.isspace()):
            raise ValueError("Contact name must be a non-empty alphabetic string.")
            
        

def check_num(number):
    
    try:
        int(number)
        
    except ValueError:
        raise InvalidPhoneNumberError("Phone number must contain digits only.")


def register_contact(phonebook, name, number):
    
    check_name(name)
    check_num(number)
    
    phonebook[name]=number
    
    return phonebook

register_contact(phonebook, name, number)

print(phonebook)
def main():

    email=input("Enter an Email: ")

    domain=email.find('@')

    if(domain==-1):
        print("Invalid")
        exit(0)

    domain_name = email[domain+1: ]

    print(email)
    print(domain)
    print(domain_name)


    

main()
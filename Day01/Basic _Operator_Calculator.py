def main():
    while True:
        num1=int(input("Enter number 1: "))
        num2=int(input("Enter number 2: "))
        operator=input("Enter a ooperator: ")

        cal=0

        if num1<0 and num2<0:
            print("Enter a positive number")

        if operator == "+":
            cal=num1+num2
            print(f"{cal} is the sum of {num1} and {num2}")
        
        elif operator == "-":
            if num1>num2:
                cal=num1-num2
                print(f"{cal} is the subtraction of {num1} and {num2}")
            else:
                print(f"{num1} is smaller than {num2}")

        elif operator == "%":
            cal=num1%num2
            print(f"{cal} is the modulous of {num1} and {num2}")

        elif operator == "/":
            cal=num1/num2
            print(f"{cal} is the division of {num1} and {num2}")

        elif operator == "//":
            cal=num1//num2
            print(f"{cal} is the floor division of {num1} and {num2}")
        else:
            print("Enter a valid opeator")

        ask=input("Do you want to conitinue : YES?NO")
        if ask.lower() in ("yes","y"," "):
            continue
        break

main()
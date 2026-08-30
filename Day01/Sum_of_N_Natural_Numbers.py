def main():
    while True:
        num = int(input("Enter the Number: "))
        total = num * (num + 1)//2
        print(f"The sum of {num} is {total}")
        
        ask=input("Do you want to conitinue : YES?NO")
        if ask.lower() in ("yes","y"," "):
            continue
        break
main()

def main():
    while True:
        while True:
            num=int(input("Ënterthe number: "))

            if num<0:
                print("Please retry with positive number")
                continue 
            break

        lim= num//2
        div = 2

        while div<=lim:

            if num%div==0:
                print(f"{num} is not prime, since it is divisible by{div}")
                break
            div +=1

        else:
            print(f"{num} is a prime number")

        ask = input("Do you want to conitnue: Yes/No ")
        if ask in ("yes", "y"," "):
            continue
        break


main()
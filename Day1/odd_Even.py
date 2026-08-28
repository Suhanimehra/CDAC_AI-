def main():
    while True:
        num = int(input("Ënter a number: "))
        if num % 2==0:
            print(f"{num} is  Even")
        else:
            print(f"{num} is odd")

        ans = input("do you want to check one more number?(yes/no)[yes]")
        if ans.lower() in("yes","y",...):
            continue
        break
main()
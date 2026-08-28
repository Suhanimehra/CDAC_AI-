def main():
    num = int(input("Enter the number to generate table: "))
    for i in range(1,11):

        print(f"{num} * {i} ={num*i}" , end=" ")
        i = i+1
    
        print("")

    
    
main()
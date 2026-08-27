# num = int(input("Enter number "))

# def fib(num):
#     if num<=1:
#         return num 
#     return fib(num-1) + fib(num-2)

# for i in range(num):
#     print(fib(i),end=" ")


n= int(input("Enter a number: "))

a,b = 0 , 1

for _ in range(n):
    print(a , end=" ")
    a,b = b , a+b



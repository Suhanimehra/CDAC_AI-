def main():

    str1= input("Enter a string: ")

    count = 1
    new_str1=""

    for i in range(1,len(str1)):
        if str1[i] == str1[i-1]:
            count+= 1

        else:
            new_str1+= str1[i-1] + str(count)
            count=1

    new_str1+= str1[-1] + str(count)


    if len(str1)>len(new_str1):

        print(new_str1)

    else:
        print(str1)

    


main()
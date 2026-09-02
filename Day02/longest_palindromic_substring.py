def palindrome():

    str1=input("Enter a string: ")
    str2=""

    for i in range(len(str1)):
        for j in range(i+1 , len(str1)+1):
            sub_string=str1[i:j]
            if sub_string==sub_string[::-1]:
                if len(sub_string)>len(str2):
                    str2=sub_string
    

    print(str2)
palindrome()
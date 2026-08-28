def name():

    name=input("Enter name: ")

    words=name.split(" ")

    if len(words) >1:
        new_sen=words[0][0].upper() +". " + words[1][0].upper()+ ". " + words[2]

        print(new_sen)

    else:

        word1=words[0]

        print(word1)
    






name()
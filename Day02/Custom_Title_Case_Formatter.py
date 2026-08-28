def main():
    str1= input("Enter a Sentence: ")

    str1_updated=str1.lower()

    word = str1_updated.split(" ")

    full=""
    for w in word:
        new_word=w[0].upper() + w[1:]

        full += new_word +" "

    print(full)








main()
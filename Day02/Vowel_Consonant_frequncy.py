def main():
    while  True:
        str1=input("Enter a Sentence: ")

        print("Vowels Frequencies:")

        print("a: ",str1.lower().count("a"))
        print("e: ",str1.lower().count("e"))
        print("i: ",str1.lower().count("i"))
        print("o: ",str1.lower().count("o"))
        print("u: ",str1.lower().count("u"))

        consonants=0

        for ch in str1.lower():
            if ch.isalpha() and ch not in "aeiou":
                consonants+=1

        print("Total Consonants: ",consonants)


main()
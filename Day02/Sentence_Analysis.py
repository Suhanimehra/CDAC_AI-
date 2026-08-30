def main():
    while True:
        a = input("Enter a Sentece: ")

        count=len(a)
        print(f"'{count} is the total characters of Sentence")

        word = a.split(' ')
        total_words=len(word)
        print(f"'{total_words} is the total words of Sentence")


main()
def main():
    while True:
        score = int(input("Enter the score: "))

        if score < 0 or score > 100:
            print("Invalid Score")
        elif score >= 90:
            print("Grade A")
        elif score >= 80:
            print("Grade B")
        elif score >= 70:
            print("Grade C")
        elif score >= 60:
            print("Grade D")
        else:
            print("Grade F")


main()

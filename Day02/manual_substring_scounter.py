def main():
    str1 = input("Enter string: ")
    sub_str1 = input("Enter Substring: ")

    count = 0
    start = 0

    while True:
        pos = str1.find(sub_str1, start)

        if pos == -1:
            break

        count += 1
        start = pos + 1

    print(count)

main()

def main():
    while True:
        year=int(input("Enter the year: "))
        # month=int(input("Enter the month: "))

        if year<1:
            print(f'"Invalid value of year {year}"')
            return

        if year%400 == 0 or year%4==0 and year%100 !=0:
            print(f"{year} is a leap year")

        else:
            print(f"{year} not a leap year")

        ans= input("Do you want to contiue ? yes/no ")
        if ans.lower() in ("yes","y"," "):
            continue
        break
main()






# if month<1 or month>12:
    # print(f'"Invalid value of month {month}"')
    #  return
    
    # if month ==2 :
        # max_days=29 if year%400 == 0 or year%4==0 and year%100 !=0 else 28
            

    # elif month in (4,6,9,11):
        # max_days=30
    
    # else :
        # max_days=31

    # print(f"{month}/{year} has {max_days} days ")
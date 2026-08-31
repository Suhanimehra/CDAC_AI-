def validator():
    date=input("Enter a date: ")

    date_split=date.split('/')

    day=int(date_split[0])
    month=int(date_split[1])
    year=int(date_split[2])

    all_month=("January","February","March","April","May","June","July",
                 "August","September","October","November","December")

    max_days=()

    if month not in range(1,13):
        print(f'"Invalid value of month {month}"')

    # if month<1 or month>12:
        # print(f'"Invalid value of month {month}"')
    
    if day not in range(1,32):
        print(f'"Invalid value of date {date}"')

    
    if month ==2 :
        max_days=29 if year%400 == 0 or year%4==0 and year%100 !=0 else 28
            

    elif month in (4,6,9,11):
        max_days=30
    
    else :
        max_days=31

    if day>max_days:
        print("Invalid date ")

        return

    month_name=all_month[month-1]

    print(f"{month_name} {day} {year}")



validator()
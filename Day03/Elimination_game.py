def game():

    soldiers=int(input("Enter the number of soldiers: "))
    intervals=int(input("Enter the number of intervals: "))

    list_soldiers=list(range(1,soldiers+1))

    print(f"Soldier circle initialized: {list_soldiers}")
    pop_idx=0

    for _ in range(1, soldiers+1):
        pop_idx = (pop_idx +intervals -1) % len(list_soldiers)

        updated=list_soldiers.pop(pop_idx) 

        print("Eliminated soldier:", updated)
        print("Remaining soldiers:", list_soldiers)

        if len(list_soldiers)<=1:
            break




game()
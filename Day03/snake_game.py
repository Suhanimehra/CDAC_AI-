def snake():


    snake_board=[['.'] * 5 for _ in range(5)]
    snake_board[2][3] = 'F'

    row1=int(input("Enter row coordinate: "))

    col1=int(input("Enter col coordinate: "))

    if row1 == 2 and col1==3:
        print("YUM! the snake ate the food! ")

    snake_board[row1][col1] = 'S'

    for row in snake_board:
        print(*row)


    
snake()
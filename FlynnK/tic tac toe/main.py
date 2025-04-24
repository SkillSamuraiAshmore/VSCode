board = {'7': '', '8': '', '9': '',
         '4': '', '5': '', '6': '',
         '1': '', '2': '', '3': '',}

player1 = 'X'
count = 0
running = True

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    
while(running):
    printBoard(board)
    print("It's your turn, " player1 + ". Make your move!")
    move = input()
    
    if board[move] == ' ':
        board[move] = player1
        count += 1
    else:
        print("That place is taken. Choose another spot!")
        continue      
    # Top row
    if board['7'] == board['8'] == board['9'] != ' ':
        printBoard(board)
        print("Game over!\n")
        print("player " + player1 + " won.")
        break
    # Middle row
    elif board['4'] == board['5'] == board['6'] != ' ':
        printBoard(board)
        print("Game over!\n")
        print("player " + player1 + " won.")
        break
    # Bottom row
    elif board['1'] == board['2'] == board['3'] != ' ':
        printBoard(board)
        print("Game over!\n")
        print("player " + player1 + " won.")
        break
    # Left column
    elif board['1'] == board['4'] == board['7'] != ' ':
        printBoard(board)
        print("Game over!\n")
        print("player " + player1 + " won.")
        break
    # Middle column
    elif board['2'] == board['5'] == board['8'] != ' ':
        printBoard(board)
        print("Game over!\n")
        print("player " + player1 + " won.")
        break
    
    # Right column
    elif board['3'] == board['6'] == board['9'] != ' ':
        printBoard(board)
        print("Game over!\n")
        print("player " + player1 + " won.")
        break
    
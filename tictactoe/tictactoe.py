board = {'7':' ','8':' ','9': ' ',
        '4':' ','5':' ','6': ' ',
        '1':' ','2':' ','3': ' ' }


player = 'x'
count = 0
running = True

def printBoard(board):
    print(board['7'] + '|' + board['8'] +'|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] +'|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

while(running):
    printBoard(board)
    
    print("its your turn," + player + ".make your move")
    move = input()
    if board[move] == ' ':
        board[move] = player
        count += 1
        # Across the top row
    else:
        print("that place is taken")
        continue
    if board['7'] == board['8'] == board['9'] != ' ':
        printBoard(board)
        print("game over\n")
        print("player" + player + "won")
        break
        # middle row
    elif board['4'] == board['5'] == board['6'] != ' ':
        printBoard(board)
        print("game over\n")
        print("player" + player + "won")
        break
       # bottom row
    elif board['1'] == board['2'] == board['3'] != ' ':
        printBoard(board)
        print("game over\n")
        print("player" + player + "won")
        break
     # left column
    elif board['1'] == board['4'] == board['7'] != ' ':
        printBoard(board)
        print("game over\n")
        print("player" + player + "won")
        break
    # middle column
    elif board['2'] == board['5'] == board['8'] != ' ':
        printBoard(board)
        print("game over\n")
        print("player" + player + "won")
        break
    # right column
    elif board['3'] == board['6'] == board['9'] != ' ':
        printBoard(board)
        print("game over\n")
        print("player" + player + "won")
        break
    # left to right
    elif board['7'] == board['5'] == board['3'] != ' ':
        printBoard(board)
        print("game over\n")
        print("player" + player + "won")
        break
    # right to left
    elif board ['9'] == board['5'] == board['1'] != ' ':
        printBoard(board)
        print("game over\n")
        print("player " + player + " won")
        break
    
    
     #Tie
    if count >= 9:
        print("game over\n")
        print("Its a tie")
        
    if player == 'x':
        player = '0'
    else:
        player = 'x'
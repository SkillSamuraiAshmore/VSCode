board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

player = 'X'
count = 0
running = True

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')

while(running):
    printBoard(board)
    print("Its your turn, " + ". Make your move!")
    move = input()
    if board[move] == ' ':
        board[move] = player
        count += 1
    else:
        print("That place is taken. Choose another spot!")
        continue

    if board['7'] == board['8'] == board['9'] != ' ':
        printBoard(board)
        print("GG Game Over!/n")
        print("Player " + " won.")
        break
    elif board['4'] == board['5'] == board['6'] != ' ':
        printBoard(board)
        print("GG Game Over!/n")
        print("Player " + " won.")
        break
    elif board['1'] == board['2'] == board['3'] != ' ':
        printBoard(board)
        print("GG Game Over!/n")
        print("Player " + " won.")
        break
    elif board['1'] == board['4'] == board['7'] != ' ':
        printBoard(board)
        print("GG Game Over!/n")
        print("Player " + " won.")
        break
    elif board['2'] == board['5'] == board['8'] != ' ':
        printBoard(board)
        print("GG Game Over!/n")
        print("Player " + " won.")
        break
    elif board['3'] == board['6'] == board['9'] != ' ':
        printBoard(board)
        print("GG Game Over!/n")
        print("Player " + " won.")
        break
    elif board['7'] == board['5'] == board['3'] != ' ':
        printBoard(board)
        print("GG Game Over!/n")
        print("Player " + " won.")
        break
    elif board['9'] == board['5'] == board['1'] != ' ':
        printBoard(board)
        print("GG Game Over!/n")
        print("Player " + " won.")
        break

    if count >= 9:
        print("Game Over!\n")
        print("Its a tie!")
        break

    if player == 'X':
        player = 'O'
    else:
        player = 'X'
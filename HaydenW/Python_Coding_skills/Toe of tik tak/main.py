board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

player = 'X'
count = 0


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    
printBoard(board)

while(running):
    printBoard(board)
    print("It's your turn, " + player + ".  Make your move!!!")
    move = input()
    if board[move] == ' ':
        board[move] = player
        count += 1
    else:
        print("That place is taken. Choose another spot!!!")
        continue
    
    if board ['7'] == board['8'] == board['9'] != ' ':
        printBoard(board)
        print("Game Over!\n")
        print("Player " + player + " won.")
        
        


    

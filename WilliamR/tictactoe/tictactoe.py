board = {'7':' ','8':'','9': '',
        '4':'','5':'','6': '',
        '1':'','2':'','3': '' }


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
    if board[move] == '  ':
        board[move] = player
        count += 1
    else:
        print("that place is taken")
        continue
    if board ['7'] == board['8'] ==board['9'] !='':
        printBoard(board)
        print("game over\n")
        print("player" + player + " WON")

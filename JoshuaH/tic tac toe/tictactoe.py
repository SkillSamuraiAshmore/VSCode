board= {'1':' ', '2':' ', '3': ' ',
        '4':' ', '5':' ', '6': ' ',
        '7':' ', '8':' ', '9': ' '}
 
player = 'X'
count = 0
running = True

def printBoard(board):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        
while (running):
        printBoard(board)
        
        print("its your turn, " + player + ". make your move!")
        move = input()
        
        if board[move] == ' ' :
                board[move] = player
                count += 1
        else:
                print("that place is taken. choose another spot")
                continue
        
        if board['1'] == board['2'] == board['3'] != ' ':
                printBoard(board)
                print("gameover!/n")
                print("player" + player +"won. ")
                break
        elif board['4'] == board['5'] == board['6'] != ' ':
                printBoard(board)
                print("gameover!/n")
                print("player" + player +"won. ")
                break
        elif board['7'] == board['8'] == board['9'] != ' ':
                printBoard(board)
                print("gameover!/n")
                print("player" + player +"won. ")
                break
        if board['7'] == board['8'] == board['9'] != ' ':
                printBoard(board)
                print("gameover!/n")
                print("player" + player +"won. ")
                break
        if board['1'] == board['4'] == board['7'] != ' ':
                printBoard(board)
                print("gameover!/n")
                print("player" + player +"won. ")
                break
        if board['2'] == board['5'] == board['8'] != ' ':
                printBoard(board)
                print("gameover!/n")
                print("player" + player +"won. ")
                break
        if board['3'] == board['6'] == board['9'] != ' ':
                printBoard(board)
                print("gameover!/n")
                print("player" + player +"won. ")
                break
        if board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("gameover!/n")
                print("player" + player +"won. ")
                break
        if board['3'] == board['5'] == board['7'] != ' ':
                printBoard(board)
                print("gameover!/n")
                print("player" + player +"won. ")
                break
        
        if count >= 9:
                print("gameover!\n")
                print("its a tie")
                break
        
        if player =='X':
                player = 'O'
        else: 
                player = 'X'
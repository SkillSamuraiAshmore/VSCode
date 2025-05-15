

board = {'7': ' ','8': ' ','9': ' ',
         '4': ' ','5': ' ','6': ' ',
         '1': ' ','2': ' ','3': ' '}

player = 'X'
count = 0
running = True

def praintBoard(board):
    print(board['7']+ '|'+ board['8']+ '|'+ board['9']+ '|')
    print('-+-+-')
    print(board['4']+ '|'+ board['5']+ '|'+ board['6']+ '|')
    print('-+-+-')
    print(board['1']+ '|'+ board['2']+ '|'+ board['3']+ '|')
   
while(running):
    praintBoard(board)
    print("It's your turn, " + player + ".  Make your move!!!")
    move = input()
    if board[move] == ' ':
        board[move] = player
        count += 1
    else:
        print("That place is taken. Choose another spot!!!")
        continue 

    # across the top row
    if board ['7'] == board['8'] == board['9'] != ' ':
            praintBoard(board)
            print("Game Over!\n")
            print("Player " + player + " won.")
    # middle row
    elif board ['4'] == board['5'] == board['6'] != ' ':
            praintBoard(board)
            print("Game Over!\n")
            print("Player " + player + " won.")
    # bottom row 
    elif board ['1'] == board['2'] == board['3'] != ' ':
            praintBoard(board)
            print("Game Over!\n")
            print("Player " + player + " won.")
# left coiumn
    elif board ['1'] == board['4'] == board['7'] != ' ':
            praintBoard(board)
            print("Game Over!\n")
            print("Player " + player + " won.")      
# middle column            
    elif board ['2'] == board['5'] == board['8'] != ' ':
            praintBoard(board)
            print("Game Over!\n")
            print("Player " + player + " won.")         
# left to right
    elif board ['3'] == board['6'] == board['9'] != ' ':
            praintBoard(board)
            print("Game Over!\n")
            print("Player " + player + " won.")    

    elif board ['7'] == board['5'] == board['3'] != ' ':
            praintBoard(board)
            print("Game Over!\n")
            print("Player " + player + " won.")   
                    
    elif board ['9'] == board['5'] == board['1'] != ' ':
            praintBoard(board)
            print("Game Over!\n")
            print("Player " + player + " won.")                     

        
        
# tie 
if count >= 9:
        print("Game Over!\n")
        print("it'a tie")
        
#TODO: fix
if player='x':
        player = 'o'

















def playGame(target):
    count = 0
    players = ["Player 1", "Player 2"]
    currentPlayer = 0
    
    while count < target:
        print("It's your turn " + players[currentPlayer])
        value = input ("pick 1, 2 or 3 \n")
        
        while value not in ["1","2","3"]:
            value = input("Enter only 1, 2 or 3 \n")
        count += int (value)
        
        print("count is at " + str(count))
        currentPlayer = (currentPlayer + 1) % 2
        
        print(players[currentPlayer] + "wins")
        
def checkEndgame():
    playAgain = input("Play again? (y/n)")
    if playAgain == "y":
        return False
    else:
        return True
            
def main():
    gameOverFlag = False
    print("HOW TO PLAY \n" + 
          "Each player takes turns adding 1, 2 or 3 to the total \n" + 
          "you lose if you are the player to reach or exeed the target value")
    while gameOverFlag == False:
        gameTarget = input("what would you like to play to? \n")
        playGame(int(gameTarget))
        gameOverFlag = checkEndgame()
        
main()
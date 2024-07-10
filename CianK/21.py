def playGame(target):
    count = 0
    players = ["Player 1", "Player 2"]
    currentPlayer = 0
    
    while count < target:
        print("It's your turn " + players[currentPlayer])
        value = input("Pick 1, 2 or 3 \n")
        
        while value not in ["1", "2", "3"]:
            value = input("Enter only 1, 2 or 3 \n")
        count += int(value)
        
        print("Count is at " + str(count))
        currentPlayer = (currentPlayer + 1) % 2
        
    print(players[currentPlayer] + " WINS!")
    
def checkEndgame():
    playAgain = input("Play again? (y/n)")
    if playAgain == "y":
        return False
    else:
        return True
    
def main():
    gameOverFlag = False
    print("RUlES \n" + 
          "Each player takes turns adding 1, 2 or 3 to the total \n" +
          "You lose if you're the player to reach or exceed the target value")
    
    while gameOverFlag == False:
        gameTarget = input("What would you like to play to? \n")
        playGame(int(gameTarget))
        gameOverFlag = checkEndgame()
main()

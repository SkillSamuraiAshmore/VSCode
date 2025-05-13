def playGame(target):
    count = 0
    players = ["Player 1", "Player 2"]
    currentPlayer = 0
    while count < target:
        print("It's your turn " + players[currentPlayer])
        value = input("Pick 1, 2, 3, 4 or 5 \n")
        while value not in ["0", "1", "2", "3", "4","5", "100"]:
            value = input("Enter only 1, 2, 3, 4 or 5 \n")
        count += int(value)
        
        print("Count is at " + str(count))
        currentPlayer = (currentPlayer + 1) % 2
        
    print(players[currentPlayer] + " WINS!")
    
def checkEndgame():
    playAgain = input("Play again? (y/n)")
    if playAgain == "y" or "yes":
        return False
    else:
        return True
    
def main():
    gameOverFlage = False
    print("How to play \n" + 
          "Each player takes turns adding 1, 2, 3, 4 or 5 to the total \n" + 
          "You lose if you're the player to reach or exceed the target value")
    while gameOverFlage == False:
        gameTarget = input("What would yuo like to play to? \n")
        playGame(int(gameTarget))
        gameOverFlage = checkEndgame()
    
main()
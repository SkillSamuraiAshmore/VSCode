def playgame(target):
        count = 0
        players =["player 1","player 2"]
        curentplayer = 0
        
        while count < target:
            print("it is your turn " + players[curentplayer])
            value = input("pick 1, 2, or 3 \n")
            
            while value not in ["1","2","3"]:
                value = input("Enter only 1, 2 or 3 \n")
            count +=int(value)
            
            print("count is at " +str(count))
            curentplayer =(curentplayer + 1) % 2
            
        print(players[curentplayer] + " WINS!")
        
def  checkendgame():
        playagain = input ("play again? y/n")
        if playagain == "y":
            return False
        else:
            return True
        
def main():
    gameoverflag = False
    print("how to play \n"+
          "each player takes turns adding 1, 2 or 3 to the total \n" +
          "you lose if you you're the player to reach or exceed the target value")
    while gameoverflag == False:
        gametarget = input("what would you like to play to\n")
        playgame(int(gametarget))
        gameoverflag = checkendgame()
        
        
        
        
main()
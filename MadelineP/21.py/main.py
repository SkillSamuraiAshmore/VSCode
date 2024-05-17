def play_game(target):
    count = 0
    players = ["Player 1", "Player 2"]
    current_player = 0

    while count < target:
        print("It's your turn " + players[current_player])
        value = input("Pick 1, 2 or 3 \n")

        while value not in ["1","2","3"]:
            value = input("enter ONLY 1, 2 or 3 \n")
        count += int(value)

        print("Count is at " + str(count))
        current_player = (current_player + 1) % 2

    print(players[current_player] + " WINS!")

def check_end_game():
    play_again = input("Play again? (y/n)")
    if play_again == "y":
        return False
    else:
        return True
    
def main():
    game_over_flag = False
    print("HOW TO PLAY \n" +
          "Each player takes turns adding 1, 2, or 3 to the total \n" +
          "You lose if you're the player to reach or exceed the target value.")
    
    while game_over_flag == False:
        game_target = input("What would you like to play to \n")
        play_game(int(game_target))
        game_over_flag = check_end_game()
main()
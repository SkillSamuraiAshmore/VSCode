import random
score = ["Leaderboard"]
def game():
    print('')
    difficulty = (input("Please choose a difficulty 1, 2 or 3:1 "))
    if difficulty == '1':
        maxNumber = 10
    elif difficulty == "2":
        maxNumber = 20
    elif difficulty == '3':
        maxNumber = 30

    number = random.randint(1, maxNumber)
    lives = 6

    name = input("What is your name? ")
    print("Hello " + name + " , I am thinking of a number between 1 and " + str(maxNumber))
    
    for guessTaken in range(lives):
        print("You have " + str(lives - guessTaken) + " guesses left")
        guess = input("Take a Guess: ")
        guess = int(guess)

        if guess == number:
            print("Good job you won!")
            break
        elif guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        elif guess > maxNumber:
            print("Way too high")
    if guess != number:
        number = str(number)
        print("No, it was " + number)
        game_over()
    elif guess == number:
        if guessTaken+1 == 1:
            grammer = "guess"
        else:
            grammer = "guesses"
        number = str(number)
        print("Good job, you won. I was thinking of " + str(number) + ". You took " + str(guessTaken+1) + " " + grammer)
        
        score.append(name + " Lvl " + str(difficulty) + " - " + str(guessTaken+1) +grammer)
        final = "\n" .join(score)
        print(final)
        game_over()

def game_over():
    replay = input("Do you want to play again? y/n ")
    if replay == "y" or replay == "Y":      
        game()
    elif replay == "n" or replay == "N":
        print("Thank you for playing")
        final = "\n" .join(score)
        print(final)
    else:
        print("Invalid input")
        game_over()
game()


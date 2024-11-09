import random
score = ["leaderboard"]
def game():

    print('')
    difficulty = (input("please pick difficulty 1, 2 or 3/n"))
    if difficulty == '1':
        maxNumber = 10
    elif difficulty == '2':
        maxNumber = 20
    elif difficulty == '3':
        maxNumber = 30
        
    number = random.randint(1, maxNumber)
    lives = 6
    
    myName = input("What is your name? ")
    print("Well, " + myName + " ,i am thinking of a number between 1 and " + str(maxNumber))
    
    for guessesTaken in range(lives):
        print("you have " + str(lives - guessesTaken) + "guesses left")
        guess = input("Take a guess: ")
        guess = int(guess)
        
        if guess == number:
            print("Good job you won! ")
            break
            
        elif guess < number:
            print("Your guess is too low")
            
        elif guess < number:
            print("Your guess is too high")
        elif guess < maxNumber:
            print("Your guess is out of range")
    if guess != number:
        number = str(number)
        # print("Nope. That number is not what im thinking of. I was thinking of: " + number)
        print(f"Nope. That number is not what im thinking of. I was thinking of: {number}")
        game_over()
    elif guess ==number:
        if guessesTaken+1 == 1:
            grammar = "guess"
        else:
            grammar = "guesses"
        
        print("That is correst I was thinking of " + str(number) + "you took" + str (guessesTaken+1) + grammar)
        
        score.append(myName + "(Lvl " +str(difficulty) +") - " + str(guessesTaken+1) +grammar)
        final  = "\n".join(score)
        print(final)
        
def game_over():
    replay = input ("do you want to play again? y/n")
    if replay == "y" or replay == "Y":
        game()
    elif replay == "n" or replay == "N":
        print("Otay thanks for playing and you better come back tomorrow or a spider infestation will invade your house")
        final = "\n".join(score)
    else:
        print("invalid input")
        game_over()
        
game()
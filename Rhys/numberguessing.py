import random

score = ["LeaderBorad"]

def game():
    print('')
    difficulty = (input("Please choose a difficulty 1,2 or 3"))
    

    if difficulty == '1':
        maxNumber = 10
    elif difficulty == '2':
        maxNumber =20
    elif difficulty == '3':
        maxNumber =30

    number = random.randint(1, maxNumber)
    lives = 6

    myName = input("What is your name?")
    print("well, " + myName + " ' I am thinking of a number between 1 and " + str(maxNumber))

    for guessesTaken in range(lives):
        print("You have " + str(lives - guessesTaken) + " guesses left")
        guess = input("Take a guess: ")
        guess = int(guess)

        if guess == number:
            print("Good job you won!")
            break

        elif guess < number:
            print("Your guess is to low")

        elif guess > number:
            print("Your guess is to high")

        elif guess > maxNumber:
            print("Your guess is out of range")    

    if guess != number:
        number = str(number)
        print("Nope. That number is not that iwas thinking of. i was thinking of: " + number)
        game_over()

    elif guess ==number:
        if guessesTaken+1 == 1:
            grammar + " guess"
        else:
            grammar = "guesses"
        
        print("that is correct I was thinking of " + str(number) + " You took" + str(guessesTaken+1) + grammar)

        score.append(myName + "(Lvl " +str(difficulty) +") - " + str(guessesTaken+1) +grammar)
        final = "\n".join(score)
        print(final)
        game_over()

def game_over():
    replay = input("Do you want to play again? y/n")
    if replay == "y" or replay == "Y":
        game()
    elif replay == "n" or replay == "N":
        print("thank you for playing")
        final = "\n".join(score)
        print(final)
    else:
        print("invalid input")
        game_over()


game()
    



    
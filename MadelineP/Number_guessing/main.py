import random

score = ["LeaderBoard"]

def game():
    print('')
    difficulty = (input("Please choose a difficulty 1,2 or 3"))

    if difficulty == '1':
        maxNumber = 10
    
    elif difficulty == '2':
        maxNumber = 20
    
    elif difficulty == '3':
        maxNumber = 30

    number = random.randint(1, maxNumber)
    lives = 6

    my_name = input("what is your name? ")
    print("Well, " + my_name + " , I am thinking of a number between 1 and " + str(maxNumber))

    for guesstaken in range(lives):
        print("You have " + str(lives - guesstaken) + " guesses left")
        guess = input('Take a guess: ')
        guess = int(guess)

        if guess == number:
            print("good job! You won!")
            break
        
        elif guess < number:
            print("Your guess is too low")

        elif guess > number:
            print("Your guess is too high")

        elif guess > maxNumber:
            print("Your guess is out of range")

    if guess != number:
        number = str(number)
        print("Nope. That number is not what i was thinking of. i was thinking of: " + number)
        game_over()
    elif guess == number:
        if guesstaken + 1 == 1:
            grammar = " guess"
        else:
            grammar = " guesses"
        
        print("That is correct. I was thinking of " + str(number) + " you took " + str(guesstaken+1) + grammar)
        
        score.append(my_name + "(Lvl " + str(difficulty) +") - " + str(guesstaken+1) + grammar)
        final = "\n".join(score)
        print(final)
        game_over()

def game_over():
    replay = input("Do you want to play again? y/n")
    if replay == "y" or replay == "Y":
        game()
    elif replay == "n" or replay == "N":
        print("Thank you for playing")
        final = "\n".join(score)
        print(final)
    else:
        print("Invalid input")
        game_over  

game()
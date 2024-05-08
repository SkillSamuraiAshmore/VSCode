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
        
        elif guess < number:
            print("Your guess is too low")

        elif guess > number:
            print("Your guess is too high")

        elif guess > maxNumber:
            print("Your guess is out of range")

        

game()
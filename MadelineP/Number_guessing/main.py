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

game()
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

game()
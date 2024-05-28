import random

score = ["leaderboard"]
maxNumber = 1

difficulty = ""

def game():
    global maxNumber
    difficulty = input("please choose a difficulty 1,2 or 3 ")
    difficulty = int(difficulty)
    if difficulty == 1:
        maxNumber = 10        
    elif difficulty == 2:
        maxNumber = 20
    elif difficulty == 3:
        maxNumber = 30

def game_over():
    replay = input("Do you want to play again? y/n")
    if replay == "y" or replay == "y":
        game()
    elif replay == "n" or replay =="N":
        print (" thanks for playing")
        final = "/n".join(score)
        print(final)
    else:
        print("invalid input")
        game_over()

lives = 6

myName = input("what is your name")
print(maxNumber)
game()
number = random.randint(1, maxNumber)


print("hi" + myName + " I am thinking of a number between 1 and " + str(maxNumber))
for guesstaken in range (lives):
    print("you have" + str (lives - guesstaken) +" guesses left")
    guess = input ("take a guess:")
    guess = int(guess)
    if guess == number:
        print("Good job you won!!!!!!!!!")
        break
    elif guess < number:
        print("your guess is too low")
    elif guess > number:
        print("your guess is too high")
    if guess == number:
        print("you won")
    elif guess < number:
        print("your guess is too low")
    elif guess > number:
        print("your guess is too high")
    elif guess > maxNumber:
        print ("your guess is out of range")
    if guess != number:
        number = str(number)
        print("this is not the number i was thinking of.i was thinking of " + number )
        game_over()
    elif guess == number:
        if guesstaken+1 == 1:\
            grammar = "guess"
        else:
            grammar = "guessses"

    print("this is corect i was thinking of" + str(number) + "you took" + str(guesstaken+1) + grammar)
    score.append (myName + "(LVL" + str(difficulty)+")  -"+ str(guesstaken+1) + grammar)
    final = "/n".join(score)
    print(final)
    game_over()


game()
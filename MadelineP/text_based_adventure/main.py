import sys
import random
import time

def typewriter(message):
    for L in message:
        sys.stdout.write(L)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')

def error_handler():
    typewriter("Sorry, that's not an option. Please enter your answer again.")

def end_game(z):
    if (z == 7):
        sys.exit()
    




hp = random.randint(6, 12)

def game_over(hp):
    if hp <= 0:
        typewriter("Game over! you lost all your HP.")
        time.sleep(3)
    else:
        typewriter("You have " + str(hp) + " hp left!")

def damage(damage, hp):
    hp-= damage
    game_over(hp)

def fight_dragon():
    global hp

    typewriter("This is a tough and strong opponent, the toughest you've ever fought! Do you fight, or do you run? The choice is your's... [fight or run]: ")
    decision = input()

    if decision == "fight":
        typewriter("The dragon doesn't have a care in the world. It swipes at you, throwing you into a pit of magma.")
        damage(999, hp)
        typewriter("Ending 2...")
    elif decision == "run":
        typewriter("Your a smart one, arn't you? You drop everything and flee, disrigarding any idea of wealth and fame.")
        typewriter("You dart out of the cave, returning to the nostalgic warmth of the sun. 'how long was I in there...' you thought to yourself...")
        typewriter("Ending 1...")
    else:
        error_handler()
        fight_dragon()

  


def cavern():
    global hp 
    typewriter("Will you try to break the door down, or will you risk climbing the spring for the key? [break or climb]: ")
    decision = input()

    if decision == "break":
        typewriter("You hit the door and are in turn hit by a falling rock")
        damage(random.randint(2, 4), hp)
        cavern()
    elif decision == "climb":
        typewriter("Good climbing! You get the key and unlock the door in no time.")
        typewriter("You open the door and step through to find yourself face to face with...")
        typewriter("... A dragon...")
        fight_dragon()
    else:
        error_handler()
        cavern()

def way():
    global hp
    typewriter("You are in a cave. There are two ways you can go, left and right. Which way? [left or right]: ")
    decision = input()

    if decision == "left":
        typewriter("The left path leads you to a small cavern with a spring in the centre and a key on top of the spring.")
        typewriter("The key must lead to the small rotted door to the right of the spring.")
        cavern()


    elif decision == "right":
        typewriter("You walk down the right path, but run into some spikes.")
        damage(random.randint(1, 3), hp)
        way()
    else:
        error_handler()
        way()

def start_game():
    global hp
    typewriter("Begin the game? [yes or no]: ")
    play = input()

    if play =="yes":
        typewriter("Let's begin!")
        game_over(hp)
        way()
    else:
        typewriter("Bye!")
        sys.exit()




typewriter("Greetings and salutations, adventurer!")
start_game()

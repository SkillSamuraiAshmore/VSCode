import sys
import random
import time

def typewriter(message):
    for L in message:
        sys.stdout.write(L)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')


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

def cavern():
    global hp 
    typewriter("Will you try to break the door down, or will you risk climbing the spring for the key? [break or climb]: ")
    decision = input()

    if decision == "break":
        typewriter("You hit the door and are in turn hit by a falling rock")
        # TODO: add damage

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

def start_game():
    global hp
    typewriter("Begin the game? [yes or no]: ")
    play = input()

    if play =="yes":
        typewriter("Let's begin!")
        game_over(hp)
        way()



typewriter("Greetings and salutations, adventurer!")
start_game()

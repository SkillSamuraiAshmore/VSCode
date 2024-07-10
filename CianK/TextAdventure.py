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
    typewriter("Invalid input !:<")

hp = random.randint(6, 12)

def game_over(hp):
    if hp <= 0:
        typewriter("Game Over! You lost all your HP.")
    else:
        typewriter("You have " + str(hp) + " HP left!")

def damage(damage, hp):
    hp -= damage
    game_over(hp)

def fight_dragon():
    typewriter("This is the strongest dragon on Earth! Will you fight or flee? [fight or flee]: ")
    decision = input()

    if decision == "fight":
        typewriter("The dragon burns you to ash and you fall to your doom")
        damage(999, hp)
    elif decision == "flee":
        typewriter("You're smart and you flee outside! In the proccess you drop everything.")
    else:
        error_handler()

def cavern():
    global hp
    typewriter("Will you try to hit the door, or will you climb the spring for the key? [hit or climb]: ")
    decision = input()
    if decision == "hit":
        typewriter("You hit the door and get hitten by a falling rock.")
        damage(random.randint(3, 6), hp)
        cavern()
    elif decision == "climb":
        typewriter("You can climb and you get the key.")
        typewriter("You are greeted by a fire breathing dragon!")
        fight_dragon()
    else:
        error_handler()
        cavern()

typewriter("Greetings, Adventurer!")

def start_game():
    global hp
    typewriter("Begin the game? Y/N: ")
    play = input()

    if play == "Y":
        typewriter("Let's begin!")
        game_over(hp)
        way()
    else:
        typewriter("Bye")
        sys.exit()
def way():
    typewriter("You are in a cave. There are 2 ways you can go, left and right. Which way?: ")
    decision = input()

    if decision == "left":
        typewriter("The left path leads you to a small cavern with a spring in the centre and a key on top of the spring")
        typewriter("The key must lead to the small door on the right of the spring")
        cavern()
    elif decision == "right":
        typewriter("You fell into a pit of spikes!")
        damage(random.randint(3,6), hp)
        way()
    else:
        error_handler()
        way()

start_game()

typewriter("You have finished me. Thanks for playing this!")
import sys
import random
import time
        
decision = input

def typewriter(message):
    for l in message:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')
    
hp = random.randint(6, 12)

def game_over(hp):
    if hp <= 0:
        typewriter("game over you lost all your HP.")
        time.sleep(3)
        sys.exit()
    else:
        typewriter("you have " + str(hp) + " hp left!")
        
def damage(damage, hp):
    hp -= damage
    game_over(hp)

def fight_robot():
    typewriter("this a strong and fearless opponent! will you fight or run? [fight or run]")
    decision = input()

if decision == "fight":
    typewriter("the robot fires its rockets at you, ending you joueny instily,")
    damage(999, hp)
elif decision == "run":
    typewriter("you'ur not a fool! you drop everything and flee")

def cavern():
    global hp
    typewriter("will you try to hit the door, or will you climb the spring for the key? [hit or climb]")
    decision = input()
    
    if decision == "hit":
        typewriter("you hit the door and are in turn hit by a falling rock.")
        damage(random.randint(2, 4), hp)
        cavern()
    elif decision == "climb":
        typewriter("you are a very good climber, and you get the key to unlock the door in no time.")
        typewriter("you open the door and step through to find yourself face to face with... a huge robot!")

def way():
    global hp
    
    typewriter("You are in a cave. There are two ways you can go, left and right. Which way? [left or right]")
    decision = input()
    
    if decision == "left":
        typewriter("The left path leads you to a small cavern with a spring in the centre and a key on top of the spring")
        typewriter("The key must lead to the samll rotted door to the right of the spring.")
    elif decision == "right":
        typewriter("You walk down the right path, but run into some spikes.")
        damage(random.randint(1, 3), hp)
        way()

def start_game():
    global hp
    
    typewriter("begin the game? [yes or no]")
    play = input()
    
    if play == "yes":
        typewriter("let's begin!")
        game_over(hp)
        way()

typewriter("hello")



        
start_game()

typewriter("you have beat the game. thanks")
        

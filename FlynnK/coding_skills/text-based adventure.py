import sys
import random
import time
        

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
        typewriter("you have " + str(hp) + " left!")
        
def damage(damage, hp):
    hp -= damage
    game_over(hp)
        
typewriter("hello")

def way():
    typewriter("You are in a cave. There are tow ways you can go, left and right. Which way? [left or right]")
    decision = input()
    
    if decision == "left":
        typewriter("The left path leads you to a small cavern with a spring in the centre and a key on top of the spring")
        typewriter("The key must lead to the samll rotted door to the right of the spring.")
    elif decision == "right":
        typewriter("You walk down the right path, but run into some spikes.")
        damage(random.randint(1, 3), hp)

def start_game():
    typewriter("begin the game? [yes or no]")
    play = input()
    
    if play == "yes":
        typewriter("let's begin!")
        
start_game()
        

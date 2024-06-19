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

def start_game():
    typewriter("begin the game? [yes or no]")
    play = input()
    
    if play == "yes":
        typewriter("let's begin!")
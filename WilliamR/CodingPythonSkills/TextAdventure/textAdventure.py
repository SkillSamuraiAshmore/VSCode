import sys 
import random
import time

hp = random.randint(3,12)

def game_over(hp):
    if hp <= 0:
        typewriter(" you have failed to win i am so sorry but you must leave now because you are dead GAME OVER :( ")
        time.sleep(3)
        sys.exit
    else:
        typewriter("you have " +str(hp)+"left")
        
        

def typewriter(message):
    for l in message:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write('\n')

def damage(damage, hp):
    hp -= damage
    game_over(hp)

typewriter("hi this is a text based adventure :)")

def way():
    global hp
    
    typewriter("you are in a cave so it this basicly a ripoff of minecraft.You can go left or right.which way do you want to go?.[left or right]:")
    decision = input()
    
    if decision == "left":
        typewriter("for some reason you chose left the path leads to a small cavern with a spring or somthing inthe center and a key on that spring thing.")
        typewriter("It must lead to the tiny door to the right of the spring")
    elif    decision == "right":
        typewriter("you walk down the right path until you run into painful spike spikes why did you chose right ")
        damage(random.randint(1,2),hp)
        
def start_game():
    typewriter("do you want to play [yes or no]:")
    play = input()
    if play == "yes":
        typewriter("it is time to begin because for some reason you want to play this game")
        
        start_game()
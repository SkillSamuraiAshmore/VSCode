import sys
import random 
import time

    
def typewriter(messsage):
    for L in message:
        sys.stdout.write(L)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')
        
hp = random.randint(6, 12)

def game_over (hp):
    if hp <= 0:
            typewriter("Game Over! You lost")
            time.sleep(3)
            sys.exit
    else:
        typewriter("you have " +str(hp) + "left!")
        
def damage(damage, hp):
    hp -=damage
    game_over(hp)
    
typewriter ("Greeting and salutatoius, adventurer!")

def start_game():
    typewriter("Begin the game? [yes or no]")
    play = input

    if play =="yes":
        typewriter("Lets begin!")
        
def way():
    typewriter("you are in a cave. there are two ways you can go, left or right. which way? [left or right]:")
    decision = input()
    
    if decision == "left":
        typewriter ("the left path leads you to a small cavern with a spring ijn the center and a key on top of the spring")
        typewriter ("the spring must lead to the small rotted door to the right of the springl.")
    elif decision == "right":
        typewriter("you walk right down the path, but run into somr spikes.")
        damage(random.randint(1,3), hp) 
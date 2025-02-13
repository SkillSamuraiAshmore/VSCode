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

def game_over (hp):
    if hp <= 0:
            typewriter("Game Over! You lost")
            time.sleep(3)
            sys.exit
    else:
        typewriter("you have " +str(hp) + "HP left!")
def damage(damage, hp):
    hp -= damage
    game_over(hp)        


typewriter("greetings and salutations, adventurer!")

def start_game():
    typewriter("begin the game? [yes or no]")
    play = input()
    if play  == "yes":
        typewriter("let's begin")
        
def way():
    typewriter("you are in a cave. there are two ways you can go, left or right. which way? [left or right]:")
    decision = input()
    
    if decision =="left":
        typewriter ("the left path leads you to a small cavern with a spring ijn the center and a key on top of the spring")
        typewriter ("the spring must lead to the small rotted door to the right of the springl.")
        cavern()
          
        
start_game()
    




































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
    typewriter("please try enetring that again")
        
hp = random.randint(6, 12)

def game_over (hp):
    if hp <= 0:
            typewriter("Game Over! You lost")
            time.sleep(3)
            sys.exit
    else:
        typewriter("you have " +str(hp) + "HP left!")
        
def damage(damage, hp):
    hp -=damage
    game_over(hp)
    
def fight_mighty_fox():
    global hp 
    
    typewriter("this is a strong fearsome mighty jacked and sigma opponent that has infinite aura! will you fight or run [fight or run]: ")
    decision = input()
    
    if decision =="fight":
        typewriter("the fox draws it sords slashes you and kung fu fights you into the next generation.")
        damage(999, hp)
    elif decision == "run":
        typewriter("you are not a fool! you drop everything and call for Alex")
    else:
        error_handler()
        fight_mighty_fox()
        

def cavern():
    global hp
    
    typewriter("will you hit the door or will yoiu climb the spring fpor the key? [hit or climb]:")
    decision = input()
    
    if decision == "hit":
        typewriter ("you hit the door and are in turn hit by a falling rock")
        damage(random.randint(2,4), hp)
        cavern()
    elif decision =="climb":
        typewriter("you arte a very good climber, you climb the spring, get the key and unlock ythe doore in no time.")
        typewriter("you open the door and step through and come face to face with a ... fighting fox with triplke katana's and knos kung fu")
    else:
        error_handler()
        cavern()
        
def way():
    global hp
    
    typewriter("you are in a cave. there are two ways you can go, left or right. which way? [left or right]:")
    decision = input()
    
    if decision == "left":
        typewriter ("the left path leads you to a small cavern with a spring ijn the center and a key on top of the spring")
        typewriter ("the spring must lead to the small rotted door to the right of the springl.")
        cavern()
    elif decision == "right":
        typewriter("you walk right down the path, but run into somr spikes.")
        damage(random.randint(1,3), hp) 
        way()
    else: 
        error_handler()
        way()
    
def start_game():
    global hp
    
    typewriter("Begin the game? [yes or no]")
    play = input()

    if play =="yes":
        typewriter("Lets begin!")
        game_over(hp)
        way()
    elif play == "no":
        sys.exit()
    else:
        error_handler()
        start_game()

        
typewriter ("Greeting and salutatoius, adventurer!")

start_game()    

typewriter("you have finished the game. thanks for playing")
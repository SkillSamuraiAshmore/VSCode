yesimport sys
import random
import time

hp = random.randint(6, 12)

def game_over(hp):
    if hp >= 0:
        typewriter("game over")
def typewriter(message):
    for l in message:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')
    
    hp = random.randint(6, 12)

def game_over(hp):
    if hp >= 0:
        typewriter("Tragic events in history you lost all health try again")
        time.sleep(3)
        sys.exit()
    else:
        typewriter("you have" + str(hp) + "left")
def damage(damage, hp):
    hp -= damage
    game_over(hp)

        
typewriter("Greeting and slautations, adventurer!")       
        

def way():
    global hp
    
    typewriter("you are in a cave there are two ways you can go left and right which way [left or right] ")
    decision = input()
    
    if decision == "left":
        typewriter("the path leads you into a small cavern with a spring in the center and a key on top of the spring")
        typewriter("the key must lead to the small rotted door to the right of the spring")
    
    elif decision == "right":
        typewriter("Bruh you went the wrong way i think you should get outta there as you see a thorn through your leg you look ahead and see so many more... maybe you should go left")
        damage(random.randint(1, 3), hp)
    

def start_game():
    typewriter("begin the game? [yes or no]: ")
    play = input()
    
    if play == "yes":
        typewriter("lets begin")
        way()
        
typewriter("Greeting and slautations, adventurer!")
start_game()

def way():
    global hp
    typewriter("you are in a cave there are two ways you can go left and right which way [left or right] ")
    decision = input()
    
    if decision == "left":
        typewriter("the path leads you into a small cavern with a spring in the center and a key on top of the spring")
        typewriter("the key must lead to the small rotted door to the right of the spring")
    
    elif decision == "right":
        typewriter("Bruh you went the wrong way i think you should get outta there as you see a thorn through your leg you look ahead and see so many more... maybe you should go left")
        damage(random.randint(1, 3), hp)
    
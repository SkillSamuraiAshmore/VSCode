import sys
import random
import time

hp = random.randint(6, 12)

def game_over(hp):
    if hp >= 0:
        typewriter("you died💀💀💀")
def typewriter(message):
    for l in message:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')
    
def error_handler():   
    typewriter("uhh i did not ask that try again")
 
hp = random.randint(6, 12)

def game_over(hp):
    if hp <= 0:
        typewriter("Tragic events in history you lost all health try again")
        time.sleep(3)
        sys.exit()
    else:
        typewriter("you have" + str(hp) + "left")
        
def damage(damage, hp):
    hp -= damage
    game_over(hp) 
       
def fight_dragon():
    typewriter("oh no he big hes chunky are you brave enough to fight him or are you gonna chicken out will you [fight or run]")
    decision = input()

    if decision == "fight":
        typewriter("hey dont blame me that your to weak as he blows a unexpected smelly and i mean smelly fart ewwwwwwwwwwwww")
        damage (999, hp)
        typewriter("i guess you found ou theres no afterlife of that sorry maybe you might have new life....")
    elif decision == "run":
        typewriter("chickening out saved you for once as you see a green gas i feel lucky for you now")
    else:
        error_handler()
        fight_dragon
        
def cavern():        
    global hp
    typewriter("will you smash down the door or will you climb the spring for a key your choice... [smash or climb] ")
    decision = input() 
    if decision == "smash":
            typewriter("womp womp be a bit wiser next time because rocks fall over you bonking your head ouch that must hurt might as well watch out for the big one...")
            damage(random.randint(2,4), hp)
    elif decision == "climb":
            typewriter("your a good climber but as you open the door you face a dragon umm i think i wet my pants...")
            fight_dragon()   
    else:
        error_handler()
        cavern()   
        
# def way():
#     global hp
    
#     typewriter("you are in a cave there are two ways you can go left and right which way [left or right] ")
#     decision = input()
    
#     if decision == "left":
#         typewriter("the path leads you into a small cavern with a spring in the center and a key on top of the spring")
#         typewriter("the key must lead to the small rotted door to the right of the spring")
#         cavern()
        
#     elif decision == "right":
#         typewriter("Bruh you went the wrong way i think you should get outta there as you see a thorn through your leg you look ahead and see so many more... maybe you should go left")
#         damage(random.randint(1, 3), hp)
#         way()
    
    

def start_game():
    typewriter("begin the game? [yes or no]: ")
    play = input()
    
    if play == "yes":
        typewriter("lets begin")
        way()
    else:
        typewriter("?")
        sys.exit()

def way():
    global hp
    typewriter("you are in a cave there are two ways you can go left and right which way [left or right] ")
    decision = input()
    
    if decision == "left":
        typewriter("the path leads you into a small cavern with a spring in the center and a key on top of the spring")
        typewriter("the key must lead to the small rotted door to the right of the spring")
        cavern()
    elif decision == "right":
        typewriter("Bruh you went the wrong way i think you should get outta there as you see a thorn through your leg you look ahead and see so many more... maybe you should go left")
        damage(random.randint(1, 3), hp)
        way()
        
    else:
        error_handler()
        way()

typewriter("Greeting and slautations, adventurer!")
start_game()

typewriter("you survived i feel happy that you didnt see theres no afterlife good work")
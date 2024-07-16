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
        typewriter("you have " +str(hp)+" hp left")
        
def start_game():
    typewriter("do you want to play [yes or no]:")
    play = input()
    if play == "yes":
        game_over(hp)
        typewriter("it is time to begin because for some reason you want to play this game")
        way()
       
    else:
        typewriter("bye you are stupid you can play later when you follow instructions")
        sys.exit()
def typewriter(message):
    for l in message:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write('\n')

def damage(damage, hp):
    hp -= damage
    game_over(hp)



def fight_dragon():
    global hp
    typewriter("this dragon does not like you and nor do you like him will you prove your worth and destroy him or run away while he laghs at you because of how pathetic you are?[fight or run]")
    
    decision = input()
    if decision == "fight":
        typewriter("the dragon swipes its claws knoking you out.if that did not destroy you then the fire will ")
        damage(999, hp)
    elif decision == "run":
        typewriter("even though the dragon is laghing and you want to kill it but half of you (including the part of the brain that thinks) is not a fool and dont want to die")
        
typewriter("hi this is a text based adventure :)")
def cavern():
    global hp
    typewriter("will you bash the door and let out yor rage of being stuck to open it,you could risk it  and cimb the spring for the key you need if you are not mad [climb or hit]")
    decision = input()
    if decision == "hit":
        typewriter("you have hit the door but rocks are falling and you are hurt")
        damage(random.randint(2, 4),hp)
        way()
    elif decision == "climb":
        typewriter("you had a lot of experience climbing because you used playgrounds the way they were not built for because you new that it whould happen when you where young. now you sucsesfuly got the key and unlocked the door ")
        typewriter("when opening the door you find ... a dragon!")
        fight_dragon()

def way():
    global hp
    
    typewriter("you are in a cave so it this basicly a ripoff of minecraft.You can go left or right.which way do you want to go?.[left or right]:")
    decision = input()
    
    if decision == "left":
        typewriter("for some reason you chose left the path leads to a small cavern with a spring or somthing in the center and a key on that spring thing.")
        typewriter("It must lead to the tiny door to the right of the spring")
        cavern()
    elif    decision == "right":
        typewriter("you walk down the right path until you run into painful spikes  why did you chose right ")
        damage(random.randint(1,2),hp)
        way()
        
start_game()

typewriter("you have finished the game.")
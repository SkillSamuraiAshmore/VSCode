import sys
import random
import time
def typewriter(message):
    for l in message:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')
    
hp = random.randint(6,12)

def game_over(hp):
    if hp <= 0:
        typewriter("game over you died :( ")
        time.sleep(3)
        sys.exit



typewriter("hi adventurers  welcome to text based adventure :)")
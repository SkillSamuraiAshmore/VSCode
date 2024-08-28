import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

#window
win_height = 720
win_widith = 551
window = pygame.pygame.display.set_mode((win_widith, win_height))

#images
bird_images = [pygame.image.load("assets/bird_down.png"),
               pygame.image.load("assets/bird_mid.png"),
               pygame.image.load("assets/background.png")]
skyline_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")




def quit_game():
    for event in pygame.event.get():
        # exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
# game main method
def main():
    run = True
    while run:
        # quit
        quit_game
        
        # reset frame 
        window.fill((0, 0, 0))
        
        clock.tick(60)
        pygame.display.update()

main()
        
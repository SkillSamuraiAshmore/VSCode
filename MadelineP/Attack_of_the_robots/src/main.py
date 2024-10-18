import pygame
from os.path import abspath
from player import Player
# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

# KEVIN: this is better solution, remember to use the "\\"
# you can r-click "copy relative path"
background_image = pygame.image.load(abspath("MadelineP\Attack_of_the_robots\\assets\BG_Urban.png"))

main_player = Player(screen, game_width/2, game_height/2)

# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        main_player.move()
        
    
    
    
    screen.blit(background_image, (0, 0))
    
    main_player.update()

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(40)
    pygame.display.set_caption("ATTACK OF THE ROBOTS fps: " + str(clock.get_fps()))

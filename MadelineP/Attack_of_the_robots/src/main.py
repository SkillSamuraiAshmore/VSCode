import pygame
import random
from os.path import abspath
from player import Player
from projectile import water_balloon
from enemy import Enemy

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

# KEVIN: this is better solution, remember to use the "\\"
# you can r-click "copy relative path"
background_image = pygame.image.load("assets/BG_Urban.png")
#background_image = pygame.image.load("MadelineP\Attack_of_the_robots\src\\assets\BG_Urban.png")

playerGroup = pygame.sprite.Group()

projectiles_group = pygame.sprite.Group()

enemyiesGroup = pygame.sprite.Group()

Player.containers = playerGroup
water_balloon.containers = projectiles_group
Enemy.containers = enemyiesGroup

enemy_spawn_timer_max = 80
enemy_spawn_timer = 0

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
        main_player.move(1, 0)
    
    if keys[pygame.K_a]:
        main_player.move(-1, 0)
        
    if keys[pygame.K_w]:
        main_player.move(0, -1)
        
    if keys[pygame.K_s]:
        main_player.move(0, 1)
        
    if pygame.mouse.get_pressed()[0]:
        main_player.shoot()
        
    enemy_spawn_timer -= 1
    if enemy_spawn_timer <= 0:
        new_enemy = Enemy(screen, 0, 0, main_player)
        side_to_spawn = random.randint(0, 3)
        if side_to_spawn == 0:
            new_enemy.y = -new_enemy.image.get_height()
            new_enemy.x = random.randint(0, game_width)
            
        elif side_to_spawn == 1:
            new_enemy.y = game_height + new_enemy.image.get_height()
            new_enemy.x = random.randint(0, game_width)
            
        elif side_to_spawn == 2:
            new_enemy.y = random.randint(0, game_height)
            new_enemy.x = -new_enemy.image.get_width()
            
        elif side_to_spawn == 3:
            new_enemy.y = random.randint(0, game_height)
            new_enemy.x = game_width + new_enemy.image.get_width()
            
        enemy_spawn_timer = enemy_spawn_timer_max
        
     
    screen.blit(background_image, (0, 0))
    
    main_player.update()
    
   
    
    for projectile in projectiles_group:
        projectile.update()


    for enemy in enemyiesGroup:
        enemy.update(projectiles_group)
    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(40)
    pygame.display.set_caption("ATTACK OF THE ROBOTS fps: " + str(clock.get_fps()))
    
    

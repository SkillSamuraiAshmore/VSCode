import pygame
from sys import exit

from pygame.sprite import Group

pygame.init()
clock = pygame.time.Clock()

#window
win_height = 720
win_widith = 551
window = pygame.display.set_mode((win_widith, win_height))

#images
bird_images = [pygame.image.load("assets/bird_down.png"),
               pygame.image.load("assets/bird_mid.png"),
               pygame.image.load("assets/bird_up.png")]
skyline_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")

#game
scroll_speed = 1
bird__start_position = (100, 250)


    

    
    
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird__start_position 
        self.image_index = 0
        
    def update(self):
        #animate bird
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = bird_images[self.image_index // 10]
class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        
    def update (self):
        #move ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_widith:
            self.kill()
            
            
                
        
        
        
        
        


def quit_game():
    for event in pygame.event.get():
        # exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
# game main method
def main():
    
    # instaiene bird
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())

    
    
    
    x_pos_ground, y_pos_ground =0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))
    
    
    
    
    
    run = True
    while run:
        # quit
        quit_game()
        
        # reset frame 
        window.fill((0, 0, 0))
        
        #DRAW BACKGROUND   
        window.blit(skyline_image, (0, 0))
        
        if len(ground) <= 2:
            ground.add(Ground(win_widith, y_pos_ground))
            
        
        
        
#draw
        ground.draw(window)
        bird.draw(window)
        #update
        ground.update()
        bird.update()
        
        clock.tick(60)
        pygame.display.update()

main()
        
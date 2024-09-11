import pygame
from sys import exit
import random

from pygame.sprite import _Group, Group

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
        self.vel = 0
        self.flap = False
        
        
        
    def update(self, user_input): 
        #animate bird
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = bird_images[self.image_index // 10]
        
        # gravity and flap
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False
            
            
            
        # rotate bird
        self.image = pygame.transform.rotate(self.image, self.vel * -7)
        
        
                
                
                
        # user input
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0:
            print("space_pressed")
            self.flap = True
            self.vel = -7

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x,y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y, = x,y
        
    def update(self):
        # move pipe
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_widith:
            self.kill()
            
            
        
        
        
    



        
        
        
    

            
        
        
        
        
        
        

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
    
    # set up pipes
    pipe_timer = 0
    pipes = pygame.sprite.Group()
    

    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))
    
    run = True
    while run:
        # quit
        quit_game()
        
        # reset frame 
        window.fill((0, 0, 0))
        
        # user input
        user_input = pygame.key.get_pressed()
        
        #DRAW BACKGROUND   
        window.blit(skyline_image, (0, 0))
        
        if len(ground) <= 2:
            ground.add(Ground(win_widith, y_pos_ground))
            
#draw
        pipes.draw(window)
        ground.draw(window)
        bird.draw(window)
        #update
        pipes.update()
        ground.update()
        bird.update(user_input)
        
        #spawn pipes
        if pipe_timer <= 0:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(90, 130) + bottom_pipe_image.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_image))
            #TODO: finish this
            pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image))
            
            
            
        
        
        clock.tick(60)
        pygame.display.update()

main()
        
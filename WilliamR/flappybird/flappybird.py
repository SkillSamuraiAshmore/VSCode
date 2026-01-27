import pygame
from sys import exit
import random

pygame.init()
clock = pygame.time.Clock()

#window
win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))

bird_images = [pygame.image.load("assets/bird_down.png"),
               pygame.image.load("assets/bird_mid.png"),                
               pygame.image.load("assets/bird_up.png")]
background_images = pygame.image.load("assets/background.png")               
game_over_images = pygame.image.load("assets/game_over.png")                
ground_image =     pygame.image.load("assets/ground.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
start_image =   pygame.image.load("assets/start.png")                
               

               
#game

scroll_speed =  1
bird_start_position = (100, 250)
score = 0
font = pygame.font.SysFont('segoe' , 26)
game_stopped = True

class Bird(pygame.sprite.Sprite):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = bird_images[0]
      self.rect = self.image.get_rect()
      self.rect.center = bird_start_position
      self.image_index = 0
      self.vel = 0
      self.flap = False
      self.alive = True
    def update(self, user_input):
        #animate
        self.image_index += 1  
        if self.image_index >=30:
            self.image_index = 0
        self.image = bird_images[self.image_index // 10]
            
            
            
           #gravity and flap
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False        
        
        #rotate
        self.image = pygame.transform.rotate(self.image, self.vel * -7)
        
        
        # User input
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7  
    
        
                    
            
    
    
    
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y,image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type
      
      
      
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()
        global score
        if self.pipe_type == 'bottom':
            if bird_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if bird_start_position[0] > self.rect.topright[0] and not self.passed:
                self.passed = True
                score += 1   
      
class Ground(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image           
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    
    def update(self):
        #moveground
        self.rect.x -= scroll_speed
        if self.rect.x <=  -win_width:
            self.kill()


def quit_game():
    #EXIT game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            


            
#main method


def main():
    global score
    #Instantiate Bird
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())
    
    #SETUP PIPES
    pipe_timer = 0
    # FORGOT PARENTHESIS
    pipes = pygame.sprite.Group()
    
   #Instantiate initial ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))
    run = True
    while run:
        #quit
        #TODO:fix
        quit_game()
        
        #reset
        window.fill(( 0, 0, 0))
        
     #user input
        user_input = pygame.key.get_pressed()   
        
        
       
        #drawbackground
        window.blit(background_images, (0, 0))
        
        #spawn Ground
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground)) 
    
    #show score
        score_text = font.render('score:' + str(score), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20))
    
    
    
        #draw - pipes, ground and bird
        pipes.draw(window)
        ground.draw(window)
        bird.draw(window)
        
        
        
        
        # update
        if bird.sprite.alive:
            pipes.update()
            ground.update()
        bird.update(user_input)
        
       #colision detection 
        collision_pipes = pygame.sprite.spritecollide(bird.sprites()[0], pipes, False)
        collision_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
        if collision_pipes or collision_ground:
            bird.sprite.alive = False
        if collision_ground:
            window.blit(game_over_images , (win_width // 2 - game_over_images.get_width() // 2, win_height // 2 - game_over_images.get_height()))
        
        if user_input[pygame.K_r]:
            score = 0
            break
        
        
        #TODO: FIX
        # if collision_pipes or collision_ground = false:
        #     bird.sprite.alive = False
        # if collision_ground:
        #     window.blit(game_over_image, (win_width// 2 - game)
        
        
        
        #spawn pipe
        if pipe_timer <= 0 and bird.sprite.alive:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(90, 130) + bottom_pipe_image.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_image, 'top'))
            pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image, 'bottom'))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1
        
        
        clock.tick(60)
        pygame.display.update() 
  #menu      
def menu():
    
    global game_stopped   
    
    while game_stopped:
        quit_game()
        
        #draw menu
        window.fill((0, 0, 0))
        window.blit(background_images, (0, 0))
        window.blit(ground_image, Ground(0, 520))
        window.blit(bird_images[0], (100, 250))
        window.blit(start_image, (win_width // 2 - start_image.get_width() // 2,
                                  win_height // 2 - start_image.get_height() // 2))
        
        user_input = pygame.key.get_pressed()
        # TODO: fix input
        if user_input[pygame.K_space]:
            main()
            
        pygame.display.update()     

menu()
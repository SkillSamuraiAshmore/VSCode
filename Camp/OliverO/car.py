import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 80
CAR_SPEED = 5
POTHOLE_WIDTH, POTHOLE_HEIGHT = 40, 40
POTHOLE_SPEED = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Potholes!")

# Car setup
car_img = pygame.image.load("car.png")  # Replace with your car image
car_rect = car_img.get_rect()
car_rect.centerx = WIDTH // 2
car_rect.bottom = HEIGHT - 20

# Pothole setup
pothole_img = pygame.image.load("pothole.png")  # Replace with your pothole image
potholes = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def spawn_pothole():
    x = random.randint(0, WIDTH - POTHOLE_WIDTH)
    y = -POTHOLE_HEIGHT
    potholes.append(pygame.Rect(x, y, POTHOLE_WIDTH, POTHOLE_HEIGHT))

def main():
    global score
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_rect.move_ip(-CAR_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            car_rect.move_ip(CAR_SPEED, 0)

        # Move potholes
        for pothole in potholes:
            pothole.move_ip(0, POTHOLE_SPEED)
            if pothole.colliderect(car_rect):
                # Game over
                print(f"Game Over! Your score: {score}")
                pygame.quit()
                sys.exit()

        # Spawn new potholes
        if random.random() < 0.02:
            spawn_pothole()

        # Update score
        score += 10

        # Draw everything
        screen.fill(WHITE)
        screen.blit(car_img, car_rect)
        for pothole in potholes:
            screen.blit(pothole_img, pothole)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
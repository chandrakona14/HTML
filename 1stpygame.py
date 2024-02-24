import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_SIZE = 20
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 300
OBSTACLE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Ball Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Define the ball class
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), BALL_SIZE)

# Define the obstacle class
class Obstacle:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(0, HEIGHT - OBSTACLE_HEIGHT)

    def move(self):
        self.x -= OBSTACLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

# Initialize the ball and obstacles
ball = Ball()
obstacles = []

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball based on arrow key inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball.move(0, -ball.speed)
    if keys[pygame.K_DOWN]:
        ball.move(0, ball.speed)
    if keys[pygame.K_LEFT]:
        ball.move(-ball.speed, 0)
    if keys[pygame.K_RIGHT]:
        ball.move(ball.speed, 0)

    # Generate new obstacles randomly
    if random.randint(0, 100) < 2:
        obstacles.append(Obstacle(WIDTH))

    # Move and draw obstacles
    for obstacle in obstacles:
        obstacle.move()
        obstacle.draw()

    # Move and draw the ball
    ball.draw()

    # Update the display
    pygame.display.flip()

    # Clear the screen
    screen.fill(BLACK)

    # Limit frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

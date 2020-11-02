import pygame
import time

# Initialization
pygame.init()
win_width = 800
win_height = 800
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake")
game_over = False

# Colors
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Positions and Deltas (Change in positions), Snake attributes
snake_block_size = 10
x = win_width / 2
y = win_height / 2
delta_x = 0
delta_y = 0

# Clock and UI
clock = pygame.time.Clock()
fps = 30
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [win_width / 2, win_height / 2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -snake_block_size
                delta_y = 0
            elif event.key == pygame.K_RIGHT:
                delta_x = snake_block_size
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_x = 0
                delta_y = -snake_block_size
            elif event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = snake_block_size
    
    # Out of bounds check
    if x >= win_width or x <= 0 or y >= win_height or y < 0:
        game_over = True
    
    x += delta_x
    y += delta_y
    window.fill(black)
    pygame.draw.rect(window, green, [x, y, snake_block_size, snake_block_size])
    
    pygame.display.update()
    clock.tick(fps)

message("You Lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()

# https://www.edureka.co/blog/snake-game-with-pygame/ Adding the food
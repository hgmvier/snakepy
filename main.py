import pygame
import time
import random

# Initialization
pygame.init()
win_width = 800
win_height = 800
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake")

# Colors
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Positions and Deltas (Change in positions), Snake attributes
snake_block_size = 10
x_pos = win_width / 2
y_pos = win_height / 2
delta_x = 0
delta_y = 0

# Clock and UI
clock = pygame.time.Clock()
fps = 30
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("monospace", 35)

def display_score(score):
    text = score_font.render("Score: " + str(score), True, yellow)
    window.blit(text, [0, 0])

def render_snake(size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], size, size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [40, win_height / 2])

def game_loop():
    game_over = False
    game_close = False
    x_pos = win_width / 2
    y_pos = win_height / 2
    delta_x = 0
    delta_y = 0
    snake_list = []
    length_of_snake = 1
    food_x = round(random.randrange(0, win_width - snake_block_size, snake_block_size))  # We pass in the snake block's size as step to
    food_y = round(random.randrange(0, win_height - snake_block_size, snake_block_size)) # ensure that the snake's position will always match up to the fruit
    

    while not game_over:
        while game_close == True:
            window.fill(black)
            message("You Lost! Press Q to Quit or C to play again.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

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
        if x_pos >= win_width or x_pos <= 0 or y_pos >= win_height or y_pos < 0:
            game_close = True
        
        x_pos += delta_x
        y_pos += delta_y
        window.fill(black)
        pygame.draw.rect(window, white, [food_x, food_y, snake_block_size, snake_block_size])
        pygame.draw.rect(window, green, [x_pos, y_pos, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x_pos)
        snake_head.append(y_pos)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        render_snake(snake_block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x_pos == food_x and y_pos == food_y:
            food_x = round(random.randrange(0, win_width - snake_block_size, snake_block_size))
            food_y = round(random.randrange(0, win_height - snake_block_size, snake_block_size))
            length_of_snake += 1

        
        clock.tick(fps)

    pygame.quit()
    quit()


game_loop()

# Adding the fruit https://www.edureka.co/blog/snake-game-with-pygame/

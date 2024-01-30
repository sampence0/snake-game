import pygame
import random

pygame.init()
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
font = pygame.font.SysFont(None, 25)

# clock
clock = pygame.time.Clock()

# snake
snake_block_size = 10
snake_speed = 15
snake_list = []
snake_length = 1
snake_x = window_width / 2
snake_y = window_height / 2

food_block_size = 10
food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])

def draw_food(food_x, food_y):
    pygame.draw.rect(window, red, [food_x, food_y, food_block_size, food_block_size])

def display_score(score):
    text = font.render("Score: " + str(score), True, white)
    window.blit(text, [0, 0])


def game_loop():
    game_over = False
    game_close = False
    snake_x = window_width / 2
    snake_y = window_height / 2
    snake_x_change = 0
    snake_y_change = 0
    snake_list = []
    snake_length = 1
    food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0

    # game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_x_change != snake_block_size:
                    snake_x_change = -snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT and snake_x_change != -snake_block_size:
                    snake_x_change = snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP and snake_y_change != snake_block_size:
                    snake_x_change = 0
                    snake_y_change = -snake_block_size
                elif event.key == pygame.K_DOWN and snake_y_change != -snake_block_size:
                    snake_x_change = 0
                    snake_y_change = snake_block_size

        snake_x += snake_x_change
        snake_y += snake_y_change

        if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
            game_close = True

        window.fill(black)
        draw_food(food_x, food_y)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        draw_snake(snake_list)
        display_score(snake_length - 1)
        pygame.display.update()
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0
            snake_length += 1
        if game_close:
            window.fill(black)
            message = font.render("You lost! Press Q-Quit or C-Play Again", True, white)
            window.blit(message, [window_width / 6, window_height / 3])
            display_score(snake_length - 1)
            pygame.display.update()
            while game_close:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            game_loop()

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()

# basic pygame window

import time
import pygame
import random

# setup
pygame.font.init()
WIDTH = 800
HEIGHT = 600
OBJ_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)
ball_size = 15
ball_speed = 7
paddle_height = 100
paddle_width = 20
font_size = 50
paddle_speed = 10
clock = pygame.time.Clock()
game_start = True
ball_x, ball_y, ball_vel_x, ball_vel_y = WIDTH / 2, HEIGHT / 2 - ball_size, -ball_speed, -ball_speed
paddle_1_y = HEIGHT // 2 - paddle_height
paddle_1_vel = 0
paddle_1_score = 0
paddle_2_y = paddle_1_y
paddle_2_vel = 0
paddle_2_score = 0
font = pygame.font.Font('freesansbold.ttf', font_size)

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('')
run = True
# main loop
while run:
    ball_speed = random.randint(5, 10)
    score_text = f'{paddle_1_score} : {paddle_2_score}'
    text_length = len(score_text) * font_size
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle_1_vel = -paddle_speed
            if event.key == pygame.K_DOWN:
                paddle_1_vel = paddle_speed

            if event.key == pygame.K_w:
                paddle_2_vel = -paddle_speed
            if event.key == pygame.K_s:
                paddle_2_vel = paddle_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                paddle_1_vel = 0
            if event.key == pygame.K_s or event.key == pygame.K_w:
                paddle_2_vel = 0
    if ball_y-(ball_size/2) < 0:
        ball_vel_y = ball_speed
    if ball_x-(ball_size/2) < 0:
        paddle_2_score += 1
        ball_x, ball_y = WIDTH / 2, HEIGHT / 2 - ball_size
        game_start = True
        ball_vel_x = ball_speed
    if ball_y+(ball_size/2) > HEIGHT:
        ball_vel_y = -ball_speed
    if ball_x+(ball_size/2) > WIDTH:
        paddle_1_score += 1
        ball_x, ball_y = WIDTH / 2, HEIGHT / 2 - ball_size
        game_start = True
        ball_vel_x = -ball_speed
    display.fill(BG_COLOR)
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    print(paddle_1_score, paddle_2_y)
    paddle_1_y += paddle_1_vel
    paddle_2_y += paddle_2_vel

    if paddle_1_y < 0:
        paddle_1_y = 0
    if paddle_1_y+paddle_height > HEIGHT:
        paddle_1_y = HEIGHT - paddle_height

    ball = pygame.draw.circle(display, OBJ_COLOR, (ball_x, ball_y), ball_size)
    paddle_1 = pygame.draw.rect(display, OBJ_COLOR, (WIDTH-paddle_width, paddle_1_y, paddle_width, paddle_height))
    paddle_2 = pygame.draw.rect(display, OBJ_COLOR, (paddle_width-20, paddle_2_y, paddle_width, paddle_height))
    display.blit(font.render(score_text, False, OBJ_COLOR), (WIDTH / 2 - text_length+195, font_size + 5))
    pygame.draw.line(display, OBJ_COLOR, (WIDTH/2-5, 0), (WIDTH/2-5, HEIGHT), 5)
    if paddle_1.colliderect(ball):
        ball_vel_x = -ball_speed
        ball_vel_y = -ball_speed
    if paddle_2.colliderect(ball):
        ball_vel_x = ball_speed
        ball_vel_y = ball_speed
    if paddle_2_y < 0:
        paddle_2_y = 0
    if paddle_2_y+paddle_height > HEIGHT:
        paddle_2_y = HEIGHT - paddle_height
    pygame.display.update()
    if game_start:
        time.sleep(2)
    game_start = False
    clock.tick(60)

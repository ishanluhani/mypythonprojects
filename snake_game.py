import random
import pygame
import math

pygame.init()
display = pygame.display.set_mode((900, 750))
player_x = 40
player_y = 375
score = 0
snake_List = []
snake_width = 100
dira = 'left'
def text_(msg, font2):
    f = font2.render(msg, True, (0, 0, 0))
    return f, f.get_rect()
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(display, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(display, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    display.blit(textSurf, textRect)
pau = False
def un():
    global pau
    pau = False
def pause():
    global pau
    pau = True
    while pau:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pau = False
        font1 = pygame.font.Font('freesansbold.ttf', 125)
        t1 = font1.render('Paused', True, (0, 0, 0))
        display.blit(t1, (450-250, 375-100))
        button('continue', 450-250-100, 375-100-200, 100, 50, (0, 200, 0), (0, 255, 0), un)
        button('quit', 450 - 250 + 100, 375 - 100 - 200, 100, 50, (200, 0, 0), (255, 0, 0), quit)
        pygame.display.update()
apple_x = random.randint(24, 700)
apple_y = random.randint(24, 600)
pygame.draw.rect(display, (0, 0, 0), (450, 375, 50, 50))
pygame.draw.rect(display, (0, 0, 0), (apple_x, apple_y, 50, 50))
times = 35
Length_of_snake = 1
pygame.display.set_caption('snake')
bullets = []
y_change = 0
snake_block = 20
x_change = 0
block_size = 25

run = True
k = 0
def snake(block_size, snakelist):
    global game_close, k
    for XnY in snakelist:
        if XnY == snake_List[-1]:
            pygame.draw.rect(display, (0, 250, 0), [XnY[0], XnY[1], block_size, block_size])
        else:
            pygame.draw.rect(display, (0, 0, 200),[XnY[0], XnY[1], block_size, block_size])
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -1
                dira = 'left'
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 1
                x_change = 0
                dira = 'right'
            elif event.key == pygame.K_LEFT:
                x_change = -1
                dira = 'left'
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 1
                y_change = 0
                dira = 'right'
            elif event.key == pygame.K_p:
                pause()
    player_y += y_change
    player_x += x_change
    snake_Head = [player_x, player_y]
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]
    pygame.display.update()
    d_y = math.sqrt((math.pow(apple_x-player_x, 2)+math.pow(apple_y-player_y, 2)))
    if d_y < 27:
        apple_y = random.randint(24, 700)
        apple_x = random.randint(24, 600)
        score+=1
        Length_of_snake += 25
    if player_y >= 730 or player_y < 0 or player_x >= 875 or player_x < 0:
        pygame.quit()
        quit()
    snake_head = [player_x, player_y]
    for i in snake_List[:-2]:
        if i == snake_head:
            run = False
    pygame.display.update()
    display.fill((200, 200, 200))
    pygame.draw.rect(display, (255, 0, 0), (apple_x, apple_y, 25, 25))
    snake(snake_block, snake_List)
    font = pygame.font.Font('freesansbold.ttf', 25)
    t = font.render(f'score: '+str(score), True, (0,0,0))
    display.blit(t, (10, 10))
    pygame.display.update()

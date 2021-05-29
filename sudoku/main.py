import pygame
import time
from test import func
from random import choice
import requests
from tkinter import filedialog

a = eval('['+open('no_internet.txt', 'r').read()+']')
board = board_copy = []
difficulty = 'easy'
try:
    print('(1) Easy')
    print('(2) Normal')
    print('(3) Hard')
    difficulty = input('--> ')
    if difficulty == '1':
        difficulty = 'easy'
    elif difficulty == '2':
        difficulty = 'medium'
    else:
        difficulty = 'hard'
    grid = requests.get('https://sugoku.herokuapp.com/board?difficulty='+difficulty)
    board = grid.json()['board']  # 5: brown 6: green 22: blue 27: yellow
    data = str(grid.json()['board'])
    open('no_internet.txt', 'a').write(data+',')
    board_copy = grid.json()['board']
except requests.exceptions.ConnectionError:
    try:
        board = choice(a)  # 5: brown 6: green 22: blue 27: yellow
        board_copy = choice(a)
    except IndexError:
        print('No internet and No data')
        exit()
pygame.font.init()
solved = False
display = pygame.display.set_mode((580, 650))
pygame.display.set_caption('Sudoku')
block_size = 65
pos = [-1, -1]
numbers_list = {}
pixel = 10
font_m = pygame.font.Font('freesansbold.ttf', 50)
font_s = pygame.font.Font('freesansbold.ttf', 30)
timer = time.time()
clock = pygame.time.Clock()
cond = []
color = (255, 255, 255)
boxes = [[board[:3] for i in board[:3]], [i[:3] for i in board[3:6]], [i[3:6] for i in board[:3]],
         [i[3:6] for i in board[:3]], [i[3:6] for i in board[3:6]], [i[3:6] for i in board[6:9]],
         [i[6:9] for i in board[:3]], [i[6:9] for i in board[3:6]], [i[6:9] for i in board[6:9]]]

def draw_board(board_draw):
    for row, tiles in enumerate(board_draw):
        for col, tile in enumerate(tiles):
                if tile == 1:
                    display.blit(font_m.render('1', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 2:
                    display.blit(font_m.render('2', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 3:
                    display.blit(font_m.render('3', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 4:
                    display.blit(font_m.render('4', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 5:
                    display.blit(font_m.render('5', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 6:
                    display.blit(font_m.render('6', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 7:
                    display.blit(font_m.render('7', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 8:
                    display.blit(font_m.render('8', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 9:
                    display.blit(font_m.render('9', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 10:
                    display.blit(font_s.render('1', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 11:
                    display.blit(font_s.render('2', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 12:
                    display.blit(font_s.render('3', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 13:
                    display.blit(font_s.render('4', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 14:
                    display.blit(font_s.render('5', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 15:
                    display.blit(font_s.render('6', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 16:
                    display.blit(font_s.render('7', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 17:
                    display.blit(font_s.render('8', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))
                elif tile == 18:
                    display.blit(font_s.render('9', True, (pixel, pixel, pixel)),(row*block_size,col*block_size))

def draw_timer(time='0'):
    display.blit(font_m.render('time:', True, (0, 0, 0)), (180, 605))
    display.blit(font_m.render(time + ' sec',True,(0,0,0)),(330,605))


def check_overlap(board,pos,event):
    try:
        event_ch = get_numbers(event)
        board_ch = board[pos[0]][pos[1]]
        return board_ch != 0 and event_ch != 'No'
    except IndexError:
        return True


def get_block_on_mouse_clicks(mouse_x,mouse_y):
    return [mouse_x//block_size,mouse_y//block_size]


def draw_grid():
    for i in range(9):
        pygame.draw.line(display,(40,40,40),(i*block_size,0),(i*block_size,580),2)
        pygame.draw.line(display, (40, 40, 40), (0, i * block_size), (600, i * block_size),2)
        if i%3 == 0:
            pygame.draw.line(display, (0, 0, 0), (i * block_size, 0), (i * block_size, 580), 4)
            pygame.draw.line(display, (0, 0, 0), (0, i * block_size), (600, i * block_size), 4)
    pygame.draw.line(display, (0, 0, 0), (0, 580), (600, 580), 4)


def draw_rect_of_player(block):
    pygame.draw.rect(display,(0,0,255),(block[0]*block_size,block[1]*block_size,block_size,block_size),6)


def get_numbers(event):
    number = 'No'
    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
        number = 1
    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
        number = 2
    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
        number = 3
    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
        number = 4
    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
        number = 5
    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
        number = 6
    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
        number = 7
    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
        number = 8
    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
        number = 9
    return number


def check(num,row,col,box,itr):
    for _ in range(itr):
        for i in box:
            for x in i:
                if x.count(num) > 1:
                    return False
        if row.count(num) > 1:
            return False
        if col.count(num) > 1:
            return False
    return True

while not solved:
    mouse = pygame.mouse.get_pos()
    display.fill(color)
    #print(board)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            solved = True
        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = get_block_on_mouse_clicks(mouse[0],mouse[1])
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                solved = True
            if e.key == pygame.K_RIGHT:
                pos[0] += 1
            if e.key == pygame.K_LEFT:
                pos[0] -= 1
            if e.key == pygame.K_UP:
                pos[1] -= 1
            if e.key == pygame.K_DOWN:
                pos[1] += 1
            #if e.key == pygame.K_s:
             #   file_name_to_save = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("text files", '*.txt')],
              #      initialdir='/')
               # print(type(file_name_to_save))
                #open(file_name_to_save,'w').write(str(board) + ',' + str(board_copy))
            if e.key == pygame.K_l:
                file_name_to_load = filedialog.askopenfilename(filetypes=[('text files', '*.txt')])
                color = (0, 255, 0)
                board = board_copy = list(eval(file_name_to_load))
            if e.key == pygame.K_BACKSPACE:
                try:
                    numbers_list.pop(str(pos))
                    board[pos[0]][pos[1]] = 0
                except KeyError:
                    continue
            nums = get_numbers(e)
            if not check_overlap(board, pos, e):
                if str(nums).isdigit() and numbers_list.get(str(pos),'h') == 'h':
                    numbers_list[str(pos)] = nums
                    board[pos[0]][pos[1]] = nums+9
    draw_rect_of_player(pos)
    draw_grid()
    draw_board(board)
    draw_timer(str(int(time.time()-timer)))
    #draw_num_p(numbers_list)

    for i in board:
        if 0 not in i:
            cond.append(True)
        else:
            cond.append(False)
    if all(cond):
        if func(board_copy) == board:
            color = (0, 255, 0)
            time.sleep(4)
            grid = requests.get('https://sugoku.herokuapp.com/board?difficulty=easy')
            board = grid.json()['board']  # 5: brown 6: green 22: blue 27: yellow
            board_copy = grid.json()['board']
            data = str(grid.json()['board'])
            open('no_internet.txt', 'a').write(data + ',')
        else:
            color = (255, 0, 0)
    else:
        color = (255,255,255)
    cond = []
    pygame.display.update()
    clock.tick(60)


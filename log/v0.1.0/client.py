import pygame
import easygui
from pygame import *

pygame.init()

done = True

map = []

playernow=2

MOUSEDOWN = False

def reloading():
    global screen, clock, black, white, window_color,map,x,y,line_color
    x=0
    y=0
    clock = 0.0
    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    window_color = (160,82,45)
    line_color = (255,231,186)
    for i in range(13):
        map_ls=[]
        for j in range(13):
            map_ls.append(0)
        map.append(map_ls)

def init():
    global screen
    screen = pygame.display.set_mode((530, 530))
    pygame.display.set_caption("Online 五子棋 Demo")
    reloading()

init()

def canvas():
    global playernow
    screen.fill(window_color)
    nx=10
    ny=10
    for j in map[0]:
        pygame.draw.line(screen, white, (nx+15,25),(nx+15,505), 3)
        nx+=40
    nx=10
    ny=10
    for i in map:
        nx=10
        pygame.draw.line(screen, white, (25, ny+15), (505, ny+15), 3)
        for j in i:
            if j == 1:
                pygame.draw.circle(screen, white, (nx+15, ny+15), 15)
            if j == 2:
                pygame.draw.circle(screen, black, (nx+15, ny+15), 15)
            nx+=40
        ny+=40
    if MOUSEDOWN:
        nx = 10
        ny = 10
        sx=0
        sy=0
        for i in map:
            nx = 10
            sx = 0
            for j in i:
                if (nx)<=x<(nx+30) and (ny)<y<(ny+30):
                    if j == 0:
                        map[sy][sx] = playernow
                        playernow = 3 - playernow
                nx += 40
                sx +=1
            ny+=40
            sy+=1

while done:
    
    x,y=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            MOUSEDOWN = True
        if event.type == pygame.MOUSEBUTTONUP:
            MOUSEDOWN = False
    canvas()
    pygame.display.flip()
    pygame.time.delay(50)
    clock+=0.05

import sys,os
import base64
import easygui
print("测试版，请保密")

# SEs3VlQtMjNUR0ItRThLTTQtM0RIUExsaXlw

basestr=easygui.enterbox("尊敬的用户，请输入您的测试用专属LG CODE：","安全验证")
basestr=base64.b64decode(basestr.encode('utf-8'))
basestr=str(basestr,'utf-8')
if basestr[0:23] == "HK7VT-23TGB-E8KM4-3DHPL":
    # print(basestr[23:len(basestr)])
    user_name=basestr[23:len(basestr)]
else:
    easygui.msgbox("验证错误，即将退出！\n\n  获取LG CODE请联系：liyp163@163.com","错误","退出")
    sys.exit()
# print("user_name:" + user_name)
shooter = easygui.msgbox("您好，"+str(user_name)+"！\n\n    感谢你对我们的支持！","Welcome","进入游戏")

if shooter!="进入游戏":
    sys.exit()

import pygame
from pygame import *

pygame.init()
os.system("cls")
print("测试版，请保密")

done = True

map = []

playernow=2

MOUSEDOWN = False
watch_type=False

wintype=False

log=[]

def reloading():
    global clock, map,x,y,wintype,log
    global black, red, white, window_color,line_color,gold,grey,clock
    global orange
    orange=(255,69,0)
    log=[]
    x=0
    wintype=False
    y=0
    watch_type=False
    # Colors
    gold=(255,215,0)
    grey=(139,134,130)
    clock = 0.0
    # Colors
    black = (0, 0, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    window_color = (160,82,45)
    line_color = (255,231,186)
    map=[]
    
    for i in range(13):
        map_ls=[]
        for j in range(13):
            map_ls.append(0)
        map.append(map_ls)

def init():
    global screen,font,font2
    font = pygame.font.Font("font/FZSTK.TTF", 72)
    font2 = pygame.font.Font("font/FZSTK.TTF", 36)
    icon = pygame.image.load("pictures/icon.ico")
    screen = pygame.display.set_mode((530, 530))
    pygame.display.set_caption("Online 五子棋 Demo")
    pygame.display.set_icon(icon)
    reloading()

init()

def checkfull():
    global map
    for i in map:
        for j in i:
            if j==0:
                return False
    return True

def menu():
    global done,playernow
    choice=easygui.choicebox("你想要做什么？", "菜单", ["重新开始","悔棋", "退出游戏","取消"])
    if choice=="重新开始":
        reloading()
    elif choice=="悔棋":
        if len(log)>0:
            # print(log[-1][2])
            map[log[-1][1]][log[-1][0]]=0
            playernow=log[-1][2]
            log.remove(log[-1])
    elif choice=="退出游戏":
        done=False
    elif choice=="取消":
        pass

def canvas():
    global playernow,watch_type,log
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
    if MOUSEDOWN and wintype==False:
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
                        # print(playernow)
                        log.append((sx,sy,playernow))
                        map[sy][sx] = playernow
                        playernow = 3 - playernow
                nx += 40
                sx +=1
            ny+=40
            sy+=1
    
    if wintype==True and watch_type==False:
        pygame.draw.rect(screen ,grey, (167,217,200,50))
        pygame.draw.rect(screen, grey, (167,287,200,50))
        pygame.draw.rect(screen, grey, (167,357,200,50))
        if x>=160 and x<=360 and y>=210 and y<=260:
            pygame.draw.rect(screen, orange, (160,210,200,50))
            screen.blit(font2.render("重新开始",True,white),(185,212))
            if MOUSEDOWN:
                reloading()
                return
        else:
            pygame.draw.rect(screen, gold, (160,210,200,50))
            screen.blit(font2.render("重新开始",True,orange),(185,212))
        if x>=160 and x<=360 and y>=280 and y<=330:
            pygame.draw.rect(screen, orange, (160,280,200,50))
            screen.blit(font2.render("返回棋盘",True,white),(185,282))
            if MOUSEDOWN:
                watch_type=True
                return
        else:
            pygame.draw.rect(screen, gold, (160,280,200,50))
            screen.blit(font2.render("返回棋盘",True,orange),(185,282))
        if x>=160 and x<=360 and y>=350 and y<=400:
            pygame.draw.rect(screen, orange, (160,350,200,50))
            screen.blit(font2.render("悔棋一次",True,white),(185,352))
            if MOUSEDOWN:
                map[log[-1][1]][log[-1][0]]=0
                playernow=log[-1][2]
                log.remove(log[-1])
                map[log[-1][1]][log[-1][0]]=0
                playernow=log[-1][2]
                log.remove(log[-1])
                return

        else:
            pygame.draw.rect(screen, gold, (160,350,200,50))
            screen.blit(font2.render("悔棋一次",True,orange),(185,352))

def checkwin():
    global map
    for i in range(13):
        for j in range(13):
            if j+4>=13:
                continue
            if map[i][j]==1 and map[i][j+1]==1 and map[i][j+2]==1 and map[i][j+3]==1 and map[i][j+4]==1:
                return 1
            if map[i][j]==2 and map[i][j+1]==2 and map[i][j+2]==2 and map[i][j+3]==2 and map[i][j+4]==2:
                return 2
    for i in range(13):
        for j in range(13):
            if i+4>=13:
                continue
            if map[i][j]==1 and map[i+1][j]==1 and map[i+2][j]==1 and map[i+3][j]==1 and map[i+4][j]==1:
                return 1
            if map[i][j]==2 and map[i+1][j]==2 and map[i+2][j]==2 and map[i+3][j]==2 and map[i+4][j]==2:
                return 2
    for i in range(13):
        for j in range(13):
            if i+4>=13 or j+4>=13:
                continue
            if map[i][j]==1 and map[i+1][j+1]==1 and map[i+2][j+2]==1 and map[i+3][j+3]==1 and map[i+4][j+4]==1:
                return 1
            if map[i][j]==2 and map[i+1][j+1]==2 and map[i+2][j+2]==2 and map[i+3][j+3]==2 and map[i+4][j+4]==2:
                return 2
    for i in range(13):
        for j in range(13):
            if i+4>=13 or j-4<0:
                continue
            if map[i][j]==1 and map[i+1][j-1]==1 and map[i+2][j-2]==1 and map[i+3][j-3]==1 and map[i+4][j-4]==1:
                return 1
            if map[i][j]==2 and map[i+1][j-1]==2 and map[i+2][j-2]==2 and map[i+3][j-3]==2 and map[i+4][j-4]==2:
                return 2
    for i in range(13):
        for j in range(13):
            if map[i][j]==0:
                return 0
    return 3

# 调试完成后请删除
def cs():
    global map
    map[2][2]=1
    map[2][3]=1 
    map[2][4]=1
    map[2][5]=1
    map[2][6]=1

# cs()

while done:
    
    x,y=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if watch_type==True:
                    watch_type=False
                else:
                    menu()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MOUSEDOWN = True
        if event.type == pygame.MOUSEBUTTONUP:
            MOUSEDOWN = False
    canvas()
    whowin=checkwin()
    isfull=checkfull()
    if watch_type==False and whowin==1:
        Font=font.render("白棋获胜！",True,gold)
        Font2=font.render("白棋获胜！",True,grey)
        wintype=True
        screen.blit(Font2,(104,104))
        screen.blit(Font,(100,100))
    elif watch_type==False and whowin==2:
        wintype=True
        Font=font.render("黑棋获胜！",True,gold)
        Font2=font.render("黑棋获胜！",True,grey)
        screen.blit(Font2,(104,104))
        screen.blit(Font,(100,100))
    elif isfull==True:
        wintype=True
        Font=font.render("平局！",True,gold)
        Font2=font.render("平局！",True,grey)
        screen.blit(Font2,(174,104))
        screen.blit(Font,(170,100))
    else:
        wintype=False
    
    pygame.display.flip()
    pygame.time.delay(50)
    clock+=0.05
pygame.quit()
sys.exit()

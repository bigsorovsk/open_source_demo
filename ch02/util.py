'''
Created on 2015年4月12日

@author: Administrator
'''

import sys, pygame, math
from pygame.locals import *

EXIT_EVENTS = (QUIT, KEYDOWN)

pygame.init()

'''
UI参数
'''
myfont = pygame.font.Font(None, 60)
screen_size = (600, 500)
screen_color = (255, 0, 255)
screen = pygame.display.set_mode(screen_size);
screen.fill(screen_color);

object_color = (100, 100, 100)
object_width = 8
part = [False] * 5

'''
设置标题
'''
def set_caption(title):
    pygame.display.set_caption(title)

'''
检查所有part
'''
def check():
    init = True
    for p in part:
        init = init and p
    if p:
        object_color = (150, 150, 150)

'''
渲染到界面
'''            
def set_display(action):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit() 
            elif event.type == KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_1:
                    part[0] = True
                elif event.key == pygame.K_2:
                    part[1] = True
                elif event.key == pygame.K_3:
                    part[2] = True
                elif event.key == pygame.K_4:
                    part[3] = True
        action()
        pygame.display.update()































        
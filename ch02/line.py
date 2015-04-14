'''
Created on 2015年4月12日

@author: Administrator
'''

import pygame, sys
from pygame.locals import *

EXIT_EVENTS = (QUIT, KEYDOWN)

pygame.init()
screen_size = (600, 500)
screen_color = (255, 0, 255)
screen = pygame.display.set_mode(screen_size);
screen.fill(screen_color);

object_color = (0, 255, 0)

start_pos = (100, 100)
end_pos = (500, 400)

def draw_line():
    '''
    pygame.draw.line(util.screen, util.screen_color, start_pos, end_pos, 8)
    pygame.display.update()
    '''
    print ("dddd")
    
while True:
    for event in pygame.event.get():
        if event in (EXIT_EVENTS):
            sys.exit()
    pygame.draw.line(screen, screen_color, start_pos, end_pos, 8)
    pygame.display.update()






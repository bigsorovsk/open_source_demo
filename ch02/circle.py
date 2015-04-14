'''
Created on 2015-4-12
@author: Administrator
@version: 1.0
'''
'''
import sys, pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Circles")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    
    screen.fill((0, 0, 200))
    color = 255, 255, 0
    position = 300, 250
    radius = 100
    width = 10
    
    pygame.draw.circle(screen, color, position, radius, width)
    
    pygame.display.update()
'''
'''
Created on 2015-4-12
@author: Administrator
@version: 2.0
'''            
import util

util.set_caption("画个圈圈诅咒你")

color = 255, 255, 0
position = 300, 250
radius = 100
width = 10
    
def draw_circle():
    util.pygame.draw.circle(util.screen, color, position, radius, width)
    util.pygame.display.update()
    
util.set_display(draw_circle)      



































'''
Created on 2015年4月12日

@author: Administrator

@version: 1.0
'''

import util

util.set_caption("画个弧，什么是弧，你懂？")

#参数配置
color = (255, 255, 0)
position = (200, 150, 200, 200)
start_angle = util.math.radians(0)
end_angle = util.math.radians(180)
width = 8

def draw_arc():
    util.pygame.draw.arc(util.screen, color, position, start_angle, end_angle, width);
    
util.set_display(draw_arc)










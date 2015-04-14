'''
Created on 2015年4月12日

@author: Administrator
'''

import util

util.set_caption("一个简单的范例")

'''
UI参数
'''
x = 300
y = 250
radius = 200
position = ((x-radius), (y-radius), (radius*2), (radius*2))
line_left = [(x, y-radius), (x, y-radius), (x-radius, y), (x, y+radius)]
line_right = [(x+radius, y), (x-radius, y), (x, y+radius), (x+radius, y)]


'''
4个part渲染
'''
def render():
    img1 = util.myfont.render("1", True, util.object_color)
    util.screen.blit(img1, (x+radius/2-20, y-radius/2))
    img2 = util.myfont.render("2", True, util.object_color)
    util.screen.blit(img2, (x+radius/2, y-radius/2))
    img3 = util.myfont.render("3", True, util.object_color)
    util.screen.blit(img3, (x+radius/2, y-radius/2-20))
    img4 = util.myfont.render("4", True, util.object_color)
    util.screen.blit(img4, (x+radius/2-20, y-radius/2-20))


'''
根据part的boolean值显示
'''
def choose():
    for i in range(len(util.part)):
        if util.part[i]:
            start_angle = util.math.radians(90*i)
            end_angle = util.math.radians(90*(i+1))
            util.pygame.draw.arc(util.screen, util.object_color, position, start_angle, end_angle, util.object_width)
            util.pygame.draw.line(util.screen, util.object_color, (x, y), line_left[i], util.object_width)
            util.pygame.draw.line(util.screen, util.object_color, (x, y), line_right[i], util.object_width)


'''
主过程
'''
def process():
    render()
    choose()
    util.check()

'''
开始渲染
'''   
util.set_display(process)  








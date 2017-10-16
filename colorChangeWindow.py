#Erik Hansen
#10/16/2017
#colorChangeWindow.py - pops up differnet color window each time clicked

from random import randint
from ggame import *
def mouseClick(event):
    red = Color(0xff0000, 1)
    green = Color(0x00ff00,1)
    blue = Color(0x0000ff,1)
    yellow = Color(0xffff00,1)
    num = randint(1,4)
    if num == 1:
        color = red
    elif num == 2:
        color = green
    elif num == 3:
        color = blue
    else:
        color = yellow
    line = LineStyle(3,color)
    square = RectangleAsset(1000,1000,line,color)
    Sprite(square)

    

App().listenMouseEvent('click',mouseClick)
App().run()
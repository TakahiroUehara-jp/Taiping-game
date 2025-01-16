# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:20:05 2025

@author: futof
"""

BLACK = (0,0,0)

message = ['']*10
def init_message():
    for i in range(10):
        message[i] == ''
        
def set_message(msg):
    for i in range (10):
        if message[i] =='':
            message[i] = msg
            return
        for i in range(9):
            message[i] = message[i+1]
        message[9] = msg
    
def draw_text(bg,txt,x,y,fnt,col):
    sur = fnt.render(txt,True, BLACK)
    bg.blit(sur,[x+1,x+2])
    sur = fnt.render(txt,True,col)
    bg.blit(sur,[x,y])
    

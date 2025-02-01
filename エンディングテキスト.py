# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:35:20 2025

@author: futof
"""

#エンディングテキスト
ending_text =[
    "勇者コトノハマモルは魔王バリーを倒し、",
    "コトバ王国はかつての平和を取り戻した。",
    "マモルは王国の民から祝福を受けた。",
    "しかし勇者は冒険を続ける。",
    "いつ復活するか分からない魔王に備え、勇者は旅を続ける。"
    "GAME CLEAR!!おめでとう!!"
    ]

def draw_ending(screen,font):
    #エンディングを画面に表示する関数
　　　screen.fill(BLACK)
   for i in enumerate(ending_text):
       draw_text(screen,line,60,100+i*50,font,WHITE)
       
def draw_text(screen,txt,x,y,fnt,col):
    sur = fnt.render(txt,True,col)
    screen.blit(sur,[x,y])
    

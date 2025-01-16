# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:20:05 2025

@author: futof
"""

import Tkinter.Tk
import pygame
import sys
import random
from pygame.locals import *

#色の定義
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)


#画像の読み込み
imgTitle = pygame.img.load("")   #タイトル画面について

#変数の宣言
pl_x = 0
pl_y = 0  
pl_d = 0                      #プレイヤーの座標を管理
idx = 0
tmr = 0
stage = 0
welcome = 0

emy_life = 0
emy_lifemax =0

pl_lifemax = 0
pl_life = 0



MAZE_W = 11                     #ダンジョンの幅・高さの詳細は未定
MAZE_H = 9
maze = []
for y in range(MAZE_H):
    maze.append([0]*MAZE_W)

DUNGEON_W = MAZE_W*3
DUNGEON_H = MAZE_H*3

def make_dungeon() :              #ダンジョンの作成
    XP = [0,1,0,-1]
    YP = [-1,0,1,0]             #方向の設定


def move_player():                #プレイヤーの移動
    global pl_x,pl_y,pl_d,idx,tmr 
    x = pl_x
    y = pl_y
    if key[K_UP] == 1: 
        pl_d = 0
        if dungeon[pl_y-1][pl_x] != 2:
          pl_y = pl_y - 1
    if key[K_DOWN] == 1:
        pl_d = 1
        if dungeon[pl_y+1][pl_x] != 2:
          pl_y = pl_y + 1
    if key[K_LEFT] == 1: 
        pl_d = 2
        if dungeon[pl_y][pl_x-1] != 2:
          pl_x = pl_x -1
    if key[K_RIGHT] == 1: 
        pl_d = 3 
        if dungeon[pl_y][pl_x+1] != 2:
          pl_x = pl_x + 1
    idx = 1
    tmr = 0      #フレームを初期値に

def draw_text(bg,txt,x,y,fnt,col):
    sur = fnt.render(txt)

def init_battle():
    emy_name 
    emy_life = emy_lifemax

message = [""]*10 　　　　　　　#1/16変更
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
    

def main():
    pygame.init()
    pygame.set_caption("Taiping Game")
    screen = pygame.display.set_mode ((880,720))    #後に調整する必要性あり
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,40)                #後に調整する必要性あり
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        tmr =tmr +1                             #フレームごとにインクリメント
        key = pygame.key.get_pressed()
    
        if idx == 0:                                   
            if tmr == 1: 
               screen.fill(BLACK)
               screen.blit(imgTitle,[40,60])
        if key[K_SPACE] == 1:
           make_dungeon()
           stage = 1
           welcome = 20
           pl_lifemax = 100
           pl_life = pl_lifemax
           idx = 1
           
        elif idx == 1:
           move_player(key)
           if welcome > 0:
               welcome = welcome - 1
               draw_text(screen,"ステージ""+""を攻略せよ".format(),300,180,font,CYAN)
       
        
        elif idx == 6: #勝利"  
           if tmr == 1:
               set_message("～"+"を倒しました")
           if tmr == 20:
               idx = 1
               tmr = 0
               
        elif idx == 7: #敗北
            if tmr == 1:
                set_messeage("やられてしまった！")
            if tmr == 11:
                idx = 8
                tmr = 29
        
        elif idx == 8: #ゲームオーバー
            if tmr == 30:
                draw_text(screen,"あなたの負けです",360,240,font,RED)
                draw_text(screen,"ゲームオーバー",360,380,font,RED)
            elif tmr == 100: 
                idx = 0
                tmr = 0

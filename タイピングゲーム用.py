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
title = pygame.image.load("picture/title.png")   #タイトル画面について
player = pygame.image.load("picture//player.png")
wall = pygame.image.load("picture//wall.png")
floor = pygame.image.load("picture//floor.png")
door = pygame.image.load("picture//door.png")
enemy1 = pygame.image.load("picture//enemy lv1.png")
enemy2 = pygame.image.load("picture//enemy lv2.png")
enemy3 = pygame.image.load("picture//enemy lv3.png")
enemy4 = pygame.image.load("picture//enemy lv4.png")
enemy5 = pygame.image.load("picture//enemy lv5.png")
key1 = pygame.image.load("picture//key1.png")
key2 = pygame.image.load("picture//key2.png")
key3 = pygame.image.load("picture//key3.png")
key4 = pygame.image.load("picture//key4.png")

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


enemies = [enemy1,enemy2,enemy3,enemy4,enemy5]

#フロア生成
def make_floor():
    make_floor = [
        [1,1,1,1,4,1,1,1,1],
        [1,0,0,0,3,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,1,1,1,2,1,1,1,1]
        ]
              
    for y in range(7):
        for x in range(9):
            if make_floor[y][x] == 0:
                bg.blit(floor,[x*110,y*80])
            if make_floor[y][x] == 1:
                bg.blit(wall,[x*110,y*80])
            if make_floor[y][x] == 2:
                bg.blit(player,[x*110,y*80])
            if make_floor[y][x] == 3:
                bg.blit(enemies[stage-1],[x*110,y*80])
            if make_floor[y][x] == 4:
                bg.blit(door,[x*110,y*80])
                


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

message = [""]*10
def set_messeage():
    for i in range():
        if message[i] == "":
            message[i] == msg
    


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
           make_floor()
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

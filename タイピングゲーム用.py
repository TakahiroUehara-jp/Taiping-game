# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:20:05 2025

@author: futof
"""
print ('a')

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

        elif idx == 2: # 画面切り替え
            draw_dungeon(screen, fontS)
            if 1 <= tmr and tmr <= 5:
                h = 80*tmr
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
            if tmr == 5:
                stage = stage + 1
                welcome = 15
                make_dungeon()
                put_event()
            if 6 <= tmr and tmr <= 9:
                h = 80*(10-tmr)
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
            if tmr == 10:
                idx = 1
                
        elif idx == 3:# プレイヤーのターン（入力待ち）
            draw_battle(screen, fontS)
            if tmr == 1: set_message("文字を")
            if battle_command(screen, font, key) == True:
                for char in dic_score[]:
                    if moji == i
                

        elif idx == 4: # プレイヤーの攻撃
            draw_battle(screen, fontS)
            if tmr == 1:
                dmg = mojisuu
            if 2 <= tmr and tmr <= 4:
                screen.blit(imgEffect[0], [700-tmr*120, -100+tmr*120])
            if tmr == 5:
                emy_blink = 5
                set_message(str(dmg)+"pts of damage!")
            if tmr == 11:
                emy_life = emy_life - dmg
                if emy_life <= 0:
                    emy_life = 0
                    idx = 6
                    tmr = 0
            if tmr == 16:
                idx = 3
                tmr = 0

        elif idx == 5: # 敵の攻撃
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("タイプミス")
            if tmr == 5:
                set_message(emy_name + " の攻撃")
                emy_step = 30
            if tmr == 9:
                dmg = emy_str + random.randint(0, 9)
                set_message(str(dmg)+"ダメージ!")
                dmg_eff = 5
                emy_step = 0
            if tmr == 15:
                pl_life = pl_life - dmg
                if pl_life < 0:
                    pl_life = 0
                    idx = 7
                    tmr = 0
            if tmr == 20:
                idx = 3
                tmr = 0
       
        
        elif idx == 6: #勝利"  
           if tmr == 1:
               set_message("～"+"を倒しました。プレイヤーの体力を10回復しました")
               if pl_life <= 90:
                   pl_life = pl_life + 10
           if tmr == 20:
               set_message("扉のカギを入手しました")
               key = key + 1
            if tmr == 28
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

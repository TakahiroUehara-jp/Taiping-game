# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:20:05 2025

@author: futof
"""

import tkinter as tk
import pygame
import sys
import random
from pygame.locals import *

#色の定義
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
CYAN  = (0,255,255)

#画像の読み込み
title = pygame.image.load("picture\\Tittle Screan(2).png")#770×769
player = pygame.image.load("picture\\player.png")
wall = pygame.image.load("picture\\wall.png")
floor = pygame.image.load("picture\\floor.png")
door = pygame.image.load("picture\\door.png")
enemy1 = pygame.image.load("picture\\enemy lv1.png")
enemy2 = pygame.image.load("picture\\enemy lv2.png")
enemy3 = pygame.image.load("picture\\enemy lv3.png")
enemy4 = pygame.image.load("picture\\enemy lv4.png")
enemy5 = pygame.image.load("picture\\enemy lv5.png")
key1 = pygame.image.load("picture\\key1.png")
key2 = pygame.image.load("picture\\key2.png")
key3 = pygame.image.load("picture\\key3.png")
key4 = pygame.image.load("picture\\key4.png")

#変数の宣言
pl_x = 5
pl_y = 9                      #プレイヤーの座標を管理
pl_d = 0                      #向き
idx = 0
tmr = 0
stage = 0
welcome = 0

emy_life = 0
emy_lifemax =0
emy_blink = 0
dmg_eff = 0

pl_lifemax = 0
pl_life = 0


enemies = [enemy1,enemy2,enemy3,enemy4,enemy5]


# フロアマップ（0: 床, 1: 壁, 2: ドア, 3: 敵）
floor_map = [
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
]

def draw_floor(screen):
    """フロアの描画"""
    for y, row in enumerate(floor_map):
        for x, tile in enumerate(row):
            X, Y = x * 70, y * 70
            if tile == 0:
                screen.blit(floor, (X, Y))
            elif tile == 1:
                screen.blit(wall, (X, Y))
            elif tile == 2:
                screen.blit(door, (X, Y))
            elif tile == 3:
                screen.blit(enemies[stage-1], (X, Y))
            # プレイヤーの描画
            if x == pl_x and y == pl_y:
                screen.blit(player, (X, Y))

def draw_battle(screen, font):
    """戦闘画面の描画"""
    screen.fill(BLACK)
    draw_text(screen, "戦闘中！", 160, 100, font, WHITE)
    draw_text(screen, f"敵のHP:{enemy_life}", 160, 150, font, RED)
    draw_text(screen, "スペースキーで攻撃", 100, 250, font, CYAN)
            
def put_event():
    global pl_x, pl_y
    for y in range(len(floor_map)):
        for x in range(len(floor_map[y])):
            X = x*70
            Y = y*70
            if floor_map[pl_y][pl_x] == 3:


                
def move_player(): #主人公の移動
    global idx, tmr, pl_x, pl_y, pl_d, pl_a, pl_life
    
    if floor_map[pl_y][pl_x] == 4: # 扉を開けた
        idx = 2
        tmr = 0
        
    if floor_map[pl_y][pl_x] == 4: # 扉を開けた
        idx = 2
        tmr = 0
        return

    
    # 方向キーで上下左右に移動
    x = pl_x
    y = pl_y
    if key[K_UP] == 1:
        pl_d = 0
        if floor_map[pl_y-1][pl_x] != 1:
            pl_y = pl_y - 1
    if key[K_DOWN] == 1:
        pl_d = 1
        if floor_map[pl_y+1][pl_x] != 1:
            pl_y = pl_y + 1
    if key[K_LEFT] == 1:
        pl_d = 2
        if floor_map[pl_y][pl_x-1] != 1:
            pl_x = pl_x - 1
    if key[K_RIGHT] == 1:
        pl_d = 3
        if floor_map[pl_y][pl_x+1] != 1:
            pl_x = pl_x + 1
    pl_a = pl_d*2
    
     
     
def draw_text(screen,txt,x,y,fnt,col):
    sur = fnt.render(txt,True,BLACK)
    screen.blit(sur,[x+1,y+2])
    sur = fnt.render(txt,True,col)
    screen.blit(sur,[x,y])
    
    
def init_battle():
    global emy_name,emy_lifemax,emy_life,emy_x,emy_y
    typ = stage
    emy_name = enemy + "lv" + str(stage)
    emy_life = emy_lifemax
    emy_x = 440
    emy_y = 560


def draw_battle(bg, fnt): # 戦闘画面の描画
    global emy_blink, dmg_eff
    bx = 0
    by = 0
    if dmg_eff > 0:
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    bg.blit(BtlBG, [bx, by])
    if emy_life > 0 and emy_blink%2 == 0:
        bg.blit(enemies[stage - 1], [emy_x, emy_y+emy_step])
    draw_bar(bg, 340, 580, 200, 10, emy_life, emy_lifemax)
    if emy_blink > 0:
        emy_blink = emy_blink - 1
    for i in range(10): # 戦闘メッセージの表示
        draw_text(bg, message[i], 600, 100+i*50, fnt, WHITE)
    draw_para(bg, fnt) # 主人公の能力を表示

# 戦闘メッセージの表示処理
message = [""]*10
def init_message():
    for i in range(10):
        message[i] = ""
    
def set_message(msg):
    for i in range(10):
        if message[i] == "":
            message[i] = msg
            return
    for i in range(9):
        message[i] = message[i+1]
    message[9] = msg

def check_answer():
    user_input = entry.get()
    if user_input == target_string.get():
        result_label.config(text="正解！", fg="black")
    else:
        result_label.config(text="不正解", fg="red")
    new_target()

def new_target():
    new_string = generate_random_string()
    target_string.set(new_string)
    entry.delete(0, tk.END)



def main():
    global idx,tmr,stage,welcome
    global pl_a,pl_life,pl_lifemax
    global emy_life,emy_lifemax,emy_blink,dmg_eff
    dmg = 0
    
    pygame.init()
    pygame.display.set_caption("Taiping Game")
    screen = pygame.display.set_mode ((770,700))    #後に調整する必要性あり
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,40)                #後に調整する必要性あり
    fontS = pygame.font.Font(None,30) 
    
    while True:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE and idx == 0:
                    draw_floor()
                    stage = 1
                    welcome = 20
                    pl_lifemax = 100
                    pl_life = pl_lifemax
                    idx = 1
                   
        tmr = tmr + 1                            #フレームごとにインクリメント
    
        if idx == 0:                                   
            if tmr == 1: 
                screen.blit(title, (30, 5))
                draw_text(screen, "Press SPACE to Start", 250, 260, font, RED)
                if pygame.key.get_pressed()[K_SPACE]:
                    idx = 1
                    tmr = 0
                    stage = 1
        
        elif idx == 1:
           move_player(key)
           draw_floor(screen,fontS)
           if welcome > 0:
               welcome = welcome - 1
               draw_text(screen,"ステージ"+"{stage}"+"を攻略せよ",300,180,font,CYAN)
           else:    
               put_event()
               if floor_map[pl_y][pl_x] == 4:  
                   idx = 2 
                   tmr = 0
                   
        elif idx == 2: # 画面切り替え
           draw_floor(screen, fontS)
           if 1 <= tmr and tmr <= 5:
                h = 80*tmr
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
           if tmr == 5:
                stage = stage + 1
                welcome = 15
                draw_floor()
                put_event()
           if 6 <= tmr and tmr <= 9:
                h = 80*(10-tmr)
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
           if tmr == 10:
                idx = 1
                
        elif idx == 3:# プレイヤーのターン（入力待ち）
            draw_battle(screen, fontS)
            if tmr == 1: 
                set_message("文字を")
            if tmr == 15:
                user_input = entry.get()
                if user_input == "正解":  # ここで正解の判定を行います
                    label.config(fg="black")  # 文字の色を黒色に変更します
                    tmr = 0
                else:
                    label.config(fg="red")  # 不正解の場合は赤色に変更します
                    tmr = 0

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
           if tmr == 28:
              idx = 1
              tmr = 0
               
        elif idx == 7: #敗北
            if tmr == 1:
                set_messeage("やられてしまった！")
            if tmr == 11:
                idx = 8
                tmr = 29
        
        elif idx == 8: #ゲームオーバー
            if tmr <= 30:
                draw_text(screen,"あなたの負けです",360,240,font,RED)
                draw_text(screen,"ゲームオーバー",360,380,font,RED)
            elif tmr == 100: 
                idx = 0
                tmr = 0

        elif idx == 10: # 戦闘開始
            if tmr == 1:
                init_battle()
                init_message()
            elif tmr <= 4:
                bx = (4-tmr)*220
                by = 0
                screen.blit(BtlBG, [bx, by])
                draw_text(screen, "Encounter!", 350, 200, font, WHITE)
            elif tmr <= 16:
                draw_battle(screen, fontS)
                draw_text(screen, emy_name+" appear!", 300, 200, font, WHITE)
            else:
                idx = 11
                tmr = 0
            
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()

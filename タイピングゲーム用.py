# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:32:30 2025

@author: owner
"""

import pygame
import sys
import random
from pygame.locals import *
import tkinter as tk
from tkinter import simpledialog

#色の定義
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
CYAN  = (0,255,255)

#画像の読み込み

title = pygame.image.load("picture2\\Tittle Screan.png")#770×769
player = pygame.image.load("picture2\\player.png")
wall = pygame.image.load("picture2\\wall.png")
floor = pygame.image.load("picture2\\floor.png")
door = pygame.image.load("picture2\\door.png")
btlbg = pygame.image.load("picture2\\btlbg.png")

enemy1 = pygame.image.load("picture2\\enemy lv1.png")
enemy2 = pygame.image.load("picture2\\enemy lv2.png")
enemy3 = pygame.image.load("picture2\\enemy lv3.png")
enemy4 = pygame.image.load("picture2\\enemy lv4.png")
enemy5 = pygame.image.load("picture2\\enemy lv5.png")

Enemy1 = pygame.image.load("picture2\\enemy lv1 (2).png")
Enemy2 = pygame.image.load("picture2\\enemy lv2 (2).png")
Enemy3 = pygame.image.load("picture2\\enemy lv3 (2).png")
Enemy4 = pygame.image.load("picture2\\enemy lv4 (2).png")
Enemy5 = pygame.image.load("picture2\\enemy lv5 (2).png")

key1 = pygame.image.load("picture2\\key1.png")
key2 = pygame.image.load("picture2\\key2.png")
key3 = pygame.image.load("picture2\\key3.png")
key4 = pygame.image.load("picture2\\key4.png")

Effect = pygame.image.load("picture/effect-attack.png")

#変数の宣言
pl_x, pl_y = 5, 8  # プレイヤーの初期タイル座標
idx = 0  # ゲーム状態
tmr = 0  # タイマー
stage = 1
welcome = 0
key = 0
check = 0
emy_name =""
enemy_life = 0
enemy_lifemax = 10*stage 
emy_blink = 0
emy_x = 0 
emy_y = 0
dmg_eff = 0
dmg = 0

pl_lifemax = 100
pl_life = 0

Enemies = [Enemy1,Enemy2,Enemy3,Enemy4,Enemy5]#floor 小さい画像
enemies = [enemy1,enemy2,enemy3,enemy4,enemy5]#battle 大きい画像
emy_name = ["スライム","コウモリ", "死神","騎士","魔王" ]  
message = [""]*10
user_input=""


list_word = ["apple","book","cat","dog","egg","fish","grape","house",
             "ice","juice","chocolate","lemon","moon","university",
             "orange","pencil","queen","rabbit","star","tree"]

#あらすじテキスト
story_text = [
    "コトバ王国は平和なコトバで満ちあふれ、そこに住む人々は",
    "いつも笑顔で平穏な暮らしを送っていた。",
    "しかし100年前に復活した魔王バリーによって",
    "コトバ王国は侵略の脅威にさらされていた。",
    "魔王バリーはかつての先代魔王ゾーゴンの封印を解き、",
    "完全体としての魔王になり、",
    "勇者コトノハマモルは生まれ育ったコトバ王国を守るため、",
    "魔王討伐を胸に誓い旅立つのであった。"
]
    

ending_text =[
    "勇者コトノハマモルは魔王バリーを倒し、",
    "コトバ王国はかつての平和を取り戻した。",
    "マモルは王国の民から祝福を受けた。",
    "しかし勇者は冒険を続ける。",
    "いつ復活するか分からない魔王に備え、勇者は旅を続ける。",
    "",
    "GAME CLEAR!!おめでとう!!"
    ]


# フロアマップ（0: 床, 1: 壁, 2: ドア, 3: 敵）
floor_map = [
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
]


def draw_floor(screen):
    global stage,Enemy,key
    Enemy = Enemies[stage-1]
    rect_Enemy = Enemy.get_rect()
    for y, row in enumerate(floor_map):
        for x, tile in enumerate(row):
            X, Y = x * 70, y * 70
            if tile == 0:
                screen.blit(floor, (X, Y))
            elif tile == 1:
                screen.blit(wall, (X, Y))
            elif tile == 2:
                screen.blit(door, (X, Y))
            #敵の描画
            if x == 5 and y == 2:
                if key == 0:
                    rect_Enemy.center = (X + 35, Y + 35)
                    screen.blit(Enemy, rect_Enemy.topleft)
                else:
                    screen.blit(floor, (X, Y))
            # プレイヤーの描画
            if x == pl_x and y == pl_y:
                screen.blit(player, (X, Y))


def draw_text(screen, text, x, y, font, color):
    """テキストの描画"""
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def draw_story(screen, font): #あらすじを画面に表示する関数
    global stage
    screen.fill(BLACK)  # 背景を黒で塗りつぶす色とかはあとで調整
    font = pygame.font.Font("ipaexm.ttf", 25)
    if stage == 1:
        for i, line in enumerate(story_text):
            draw_text(screen, line, 60, 100 + i * 50, font, WHITE)  # テキストを1行ずつ表示
    if stage == 5:
        for i, line in enumerate(ending_text):
            draw_text(screen, line, 60, 100 + i * 50, font, WHITE)
        

def draw_bar(screen, x, y, width, height, current, maximum):
    ratio =  current/ maximum 
    # ゲージの枠を描画
    pygame.draw.rect(screen, WHITE, (x, y, width, height), 2)  # 白い枠
    fill_width = int(width * ratio)  # 現在の比率で幅を決定
    if ratio > 0.5:
        color = (0, 255, 0)  # 緑（HPが半分以上）
    elif ratio > 0.2:
        color = (255, 255, 0)  # 黄色（HPが少ない）
    else:
        color = (255, 0, 0)  # 赤（HPが非常に少ない）
    pygame.draw.rect(screen, color, (x, y, fill_width, height))  # 塗りつぶし


def draw_para(screen, font):    # プレイヤーの能力を表示
    draw_text(screen, f"HP: {pl_life}/{pl_lifemax}", 20, 20, font, WHITE)

#Fuka
def draw_battle(screen, font):
    """戦闘画面の描画"""
    global emy_blink, dmg_eff,enemies,stage
    bx = 0
    by = 60
    if dmg_eff > 0:
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    screen.blit(btlbg, [bx, by])
    enemy = enemies[stage-1]
    rect_enemy = enemy.get_rect()
    rect_enemy.center = (385, 380)
    screen.blit(enemy, rect_enemy.topleft)
    draw_bar(screen, 280, 560, 200, 10, enemy_life, enemy_lifemax)
    if emy_blink > 0:
        emy_blink = emy_blink - 1
    for i in range(10): # 戦闘メッセージの表示
        draw_text(screen, message[i], 600, 100+i*50, font, WHITE)
    draw_para(screen, font) # 主人公の能力を表示

def new_target():
    global target, answer
    target = random.choice(list_word)
    answer = target                                                            #130 12:55　たかひろ改修
    check = 0
    
def handle_user_input(event):
    """PygameのKEYDOWNイベントで文字入力を処理"""
    global user_input
    if event.key == pygame.K_BACKSPACE:
        user_input = user_input[:-1]                                         # 文字を削除
    if event.key==K_RETURN:
        None
    else:
       user_input += event.unicode                                                                        # 直接文字を追加（日本語IMEを使う場合はシステム設定
       #たかひろが改修130 12:33

def check_answer():
    """入力が正しいか確認"""
    global check, user_input, target
    if user_input.strip().lower() == target.lower():
        check = 1
    else:
        check = 2
        
        
def main():
    global idx, tmr, pl_x, pl_y,pl_life, enemy_life,dmg,target,answer,user_input,check,key,stage
    pygame.init()
    pygame.display.set_caption("Typing Game")
    screen = pygame.display.set_mode((770, 700))
    
    #ディスプレイのサイズ
    clock = pygame.time.Clock()
    font = pygame.font.Font("ipaexm.ttf", 40)
    user_input=""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                handle_user_input(event)  
                if event.key==K_RETURN:
                    check_answer()
                if event.key==K_BACKSPACE:
                    user_input=user_input[:-1]        

        tmr += 1
        screen.fill(BLACK)

        if idx == 0:  # タイトル画面
            screen.blit(title, (30, 5))
            draw_text(screen, "Press SPACE to Start", 190, 260, font, CYAN)
            keys = pygame.key.get_pressed()
            if pygame.key.get_pressed()[K_SPACE]:
                stage = 1
                welcome = 20
                pl_x, pl_y = 5, 8                                                       #変更：全クリア後の初期位置のバグ修正のため（2/1)
              
                pl_lifemax = 100
                pl_life = pl_lifemax
                idx = 1
                tmr = 0


        elif idx == 1:  # ゲーム画面（フロア探索）
            draw_floor(screen)
            keys = pygame.key.get_pressed()
            if keys[K_UP] and floor_map[pl_y - 1][pl_x] != 1 and pl_y > 0:
                pl_y -= 1
            elif keys[K_DOWN] and floor_map[pl_y + 1][pl_x] != 1 and pl_y < len(floor_map) - 1:
                pl_y += 1
            elif keys[K_LEFT] and floor_map[pl_y][pl_x - 1] != 1 and pl_x > 0:
                pl_x -= 1
            elif keys[K_RIGHT] and floor_map[pl_y][pl_x + 1] != 1 and pl_x < len(floor_map[0]) - 1:
                pl_x += 1
        
            if pl_x == 5 and pl_y == 2:
                if key == 0:
                    idx = 2
                    tmr = 0
            if pl_x == 5 and pl_y == 0:
                if key == 1:
                    stage += 1
                    key = 0
                    pl_x, pl_y = 5, 8 
                    idx = 1
                    tmr = 0
                

        elif idx == 2:#戦闘画面
            draw_battle(screen, font)
            if tmr <= 10:
                draw_text(screen, "敵に遭遇!", 300, 200, font, WHITE)
            elif tmr <= 17:
                draw_text(screen, emy_name[stage-1]+"を倒せ!", 220, 200, font, WHITE)
                enemy_life = enemy_lifemax
            else:
                idx = 3
                tmr = 0
        
                
        elif idx == 3:# プレイヤーのターン（入力待ち）
            draw_battle(screen,font)
            keys = pygame.key.get_pressed()
            if tmr == 1:
                new_target()
            else:
                draw_text(screen, f"入力する文字: {target}", 120, 200, font, WHITE)
                draw_text(screen, f"あなたが入力した文字:{user_input}", 120, 100, font, WHITE)
                
                if check == 1:
                    user_input = ""  # 入力をリセット
                    new_target()  # 新しいターゲットを設定
                    check = 0
                    idx = 4
                    tmr = 0
                elif check == 2:
                    user_input = ""  # 入力をリセット
                    check = 0
                    idx = 5
                    tmr = 0
                    

        elif idx == 4: # プレイヤーの攻撃
            draw_battle(screen,font)
            if tmr <= 10:
                draw_text(screen, "正解", 220, 300, font, WHITE)
                dmg = len(target) #変更                                              #mojisuuはタイピングの記述がないため仮置き
            if 11 <= tmr and tmr <= 40:
                screen.blit(Effect, [700-tmr*120, -100+tmr*120])
                emy_blink = 5
                draw_text(screen, "{dmg}のダメージ!", 220, 300, font, CYAN)
            else:
                enemy_life = enemy_life - dmg #変更
                if enemy_life <= 0:
                    enemy_life = 0
                    idx = 6
                    tmr = 0
                else:
                    idx = 3
                    tmr = 0

        elif idx == 5: # 敵の攻撃                                                                               #変更：前回のミーティング(1/31)をベースに再度修正（2/1)
            draw_battle(screen,font)
            if  2 <= tmr and tmr <= 12:
                draw_text(screen,"不正解！！"+ emy_name[stage-1]+"の攻撃 ", 220, 120, font, CYAN)                #変更：「不正解」と「敵の攻撃」をまとめて表示 (2/1)
                emy_step = 30
            if  13 <= tmr and tmr <= 23:
                draw_text(screen, str(stage*10)+"ダメージ受けた!", 220, 120, font, CYAN)
                emy_step = 0
            if tmr == 30:
                pl_life = pl_life - stage*10
                if pl_life <= 0:
                    idx = 7
                    tmr = 0
                else:
                    idx = 3
                    tmr = 0
       
        
        elif idx == 6: #勝利"  
           draw_battle(screen,font)
           if 1 <= tmr and tmr <= 12:
               draw_text(screen,"あなたの勝利 ", 220, 120, font, CYAN)
               if stage == 5:
                   idx = 9
                   tmr = 0
               else:   
                   if pl_life <= 90:
                       pl_life = pl_life + 10
                   else:
                       pl_life = pl_lifemax
           elif tmr <= 27:
               draw_text(screen,"扉のカギを入手しました", 210, 100, font, CYAN)
               screen.blit(key1,(250,150))
               key = 1 
           else:
               idx = 1
               tmr = 0
               pl_x, pl_y = 5, 2

               
        elif idx == 7: #敗北
            draw_battle(screen,font)
            if tmr <= 12:
                draw_text(screen,"やられてしまった", 220, 120, font, CYAN)
            else:
                idx = 8
                tmr = 0
        
        elif idx == 8: #ゲームオーバー
            draw_battle(screen,font)
            keys = pygame.key.get_pressed()
            if tmr <= 30:
                draw_text(screen,"あなたの負けです",220,120,font,RED)
                draw_text(screen,"ゲームオーバー",220,220,font,RED)
            else:
                idx = 0
                tmr = 0

        #Fuka
        elif idx == 9: #クリア
            draw_story(screen,font)
            keys = pygame.key.get_pressed()
            if tmr >= 14:
                draw_text(screen,"Press SPACE to next",320,650,font,CYAN)
                if pygame.key.get_pressed()[K_SPACE]:
                    idx = 0
                    tmr = 0
            
        elif idx == 10:
            draw_story(screen,font)
            keys = pygame.key.get_pressed()
            if tmr >= 14:
                draw_text(screen,"Press SPACE to next",320,650,font,CYAN)
                if pygame.key.get_pressed()[K_SPACE]:
                    idx = 1
                    tmr = 0
            
        pygame.display.update()
        clock.tick(7)

if __name__ == "__main__":
    main()

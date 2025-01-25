# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:41:28 2025

@author: takau
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:49:24 2025

@author: takau
"""
import pygame
import sys
import random
from pygame.locals import *

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)

# 画像の読み込み
title = pygame.image.load("picture/Tittle Screan(2).png")
player = pygame.image.load("picture/player.png")
wall = pygame.image.load("picture/wall.png")
floor = pygame.image.load("picture/floor.png")
door = pygame.image.load("picture/door.png")
enemy1 = pygame.image.load("picture/enemy lv1.png")
enemy_floor =pygame.image.load("picture/enem lvmax.jpg")
btbg=pygame.image.load("picture/btlbg.png")
# グローバル変数の初期化
pl_x, pl_y = 1, 1  # プレイヤーの初期タイル座標
idx = 0  # ゲーム状態
tmr = 0  # タイマー
pl_d = 0
pl_a = 0
stage = 0
welcome = 0
key = 0
emy_name =""
emy_life = 0
emy_lifemax = 30
emy_step = 0
emy_blink = 0
emy_x = 0 
emy_y = 0
dmg_eff = 0
user_input=""
dec_target1 = {'りんご':['r','i','n','g','o'],'ラーメン':['r','a','-','m','e','n']}




pl_lifemax = 0
pl_life = 0

def draw_bar(screen, x, y, width, height, current, maximum):
#draw_barは定義されていなかたので、仮で定義しておきました。細かな調整は後でやってね
    # ゲージの比率を計算
    ratio = current / maximum
    
    # ゲージの枠を描画
    pygame.draw.rect(screen, WHITE, (x, y, width, height), 2)  # 白い枠

    # 現在の値に応じたゲージを描画
    fill_width = int(width * ratio)  # 現在の比率で幅を決定
    if ratio > 0.5:
        color = (0, 255, 0)  # 緑（HPが半分以上）
    elif ratio > 0.2:
        color = (255, 255, 0)  # 黄色（HPが少ない）
    else:
        color = (255, 0, 0)  # 赤（HPが非常に少ない）

    pygame.draw.rect(screen, color, (x, y, fill_width, height))  # 塗りつぶし

def draw_para(screen, font):
    # プレイヤーの能力を表示
    draw_text(screen, f"HP: {pl_life}/{pl_lifemax}", 20, 20, font, WHITE)
    # 必要に応じて、攻撃力や防御力など他の能力を追加
#コメント　draw_paraが定義されていなかったので、定義しました。

def draw_battle(screen, font):
    """戦闘画面の描画"""
    global emy_blink, dmg_eff
    bx = 0
    by = 0
    if dmg_eff > 0:
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    screen.blit(btbg, [bx, by])
    if emy_life > 0 and emy_blink%2 == 0:
        screen.blit(enemies[stage-1], [emy_x, emy_y+emy_step])
    draw_bar(screen, 340, 580, 200, 10, emy_life, emy_lifemax)
    if emy_blink > 0:
        emy_blink = emy_blink - 1
    draw_para(screen, font) # 主人公の能力を表示

def draw_target(screen, font, dec_target1):
    # dec_target1のキーをランダムに選んでターゲット文字を取得
    target = random.choice(list(dec_target1.keys()))
    
    # 選ばれたターゲット文字を画面に表示
    draw_text(screen, f"入力する文字: {target}", 30, 30, font, BLACK)
        

def new_target():
    global target, current_index
    target = random.choice(list(dic_word1.keys()))  # ランダムに単語を選択
    current_index = 0  # 進行状況をリセット
    target_label.config(text=target)
    result_label.config(text="入力してください", fg="black")
    entry.delete(0, END)

def input_typing_event(event,target,user_input):
    if event.type==pygame.KEYDOWN:
        if event.Key==pygame.K_BACKSPACE:
            user_input=user_input[:-1]
            #Backspaceを押したときの処理 
        else:
            user_input += event.unicode
            return user_input,None

def check_answer():
    global target, answer, current_index
    user_input = entry.get()
    answer = dic_word1[target]
    target = random.choice(list(dec_word1.keys))
    current_index = 0
    
    if user_input == answer[current_index]:# 入力が現在の正解と一致する場合
        result_label.config(text= user_input, fg="red")
        current_index += 1  # 次の文字へ
        if current_index == len(answer):  # 全て正解した場合
            new_target()  # 新しい単語に切り替え
    else:
        None

    
    

def main():
    global idx, tmr, pl_x, pl_y, emy_life
    pygame.init()
    pygame.display.set_caption("Typing Game")
    screen = pygame.display.set_mode((770, 700))
    #ディスプレイのサイズ
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        tmr += 1
        screen.fill(BLACK)

        if idx == 0:  # タイトル画面
            screen.blit(title, (30, 5))
            draw_text(screen, "Press SPACE to Start", 230, 350, font, CYAN)
            if pygame.key.get_pressed()[K_SPACE]:
                idx = 1
                tmr = 0



        elif idx == 1:  # 戦闘画面
            draw_battle(screen, font)
            keys = pygame.key.get_pressed()
            draw_target(screen, font, dec_target1)  # ターゲット文字表
            draw_text(screen, f"あなたが入力した文字: {user_input}", 30, 100, font, CYAN)

            if keys[K_SPACE] and tmr % 10 == 0:  # スペースキーで攻撃
                emy_life -= random.randint(1, 5)
                if emy_life <= 0:
                    # 敵を倒したらフロア画面に戻る
                    emy_life = 10  # 敵のHPをリセット
                    idx = 1
                    # 敵を消す
                    floor_map[pl_y][pl_x] = 0

        pygame.display.update()
        clock.tick(10)  # 1秒間に10フレーム更新

def draw_text(screen, text, x, y, font, color):
    """テキストの描画"""
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

if __name__ == "__main__":
    main()
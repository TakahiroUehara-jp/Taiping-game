

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

pl_lifemax = 0
pl_life = 0

# フロアマップ（0: 床, 1: 壁, 2: ドア, 3: 敵）
floor_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def draw_floor(screen):
    """フロアの描画"""
    for y, row in enumerate(floor_map):
        for x, tile in enumerate(row):
#enumerateは
            X, Y = x * 70, y * 70
            if tile == 0:
                screen.blit(floor, (X, Y))
            elif tile == 1:
                screen.blit(wall, (X, Y))
            elif tile == 2:
                screen.blit(door, (X, Y))
            elif tile == 3:
                screen.blit(enemy_floor, (X, Y))
            # プレイヤーの描画
            if x == pl_x and y == pl_y:
                screen.blit(player, (X, Y))
def init_battle():
    global emy_name,emy_lifemax,emy_life,emy_x,emy_y
    typ = stage
    emy_name = enemy + "lv" + str(stage)
    emy_life = emy_lifemax
    emy_x = 440
    emy_y = 560
    
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
    for i in range(10): # 戦闘メッセージの表示
        draw_text(screen, message[i], 600, 100+i*50, font, WHITE)
    draw_para(screen, font) # 主人公の能力を表示

message = [""]*10
def init_message():
    for i in range(10):
        message[i] = ["sushi","てんぷら","らーめん","かぜ","ごま","みかん","りんご","ごりら"]
    
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
    global idx, tmr, pl_x, pl_y, enemy_life
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

        elif idx == 1:  # ゲーム画面（フロア探索）
            draw_floor(screen)
            keys = pygame.key.get_pressed()
#pygame.key.get_pressedは押されているキーをリアルタイム判定できる関数
            # プレイヤーの移動
            if keys[K_UP] and floor_map[pl_y - 1][pl_x] != 1:
                pl_y -= 1
#プレイヤーがKey_upを押して、フロアの1つ上の座標が1=壁じゃなかったら、そこに移動していいよって指示、下も同じ
            elif keys[K_DOWN] and floor_map[pl_y + 1][pl_x] != 1:
                pl_y += 1
            elif keys[K_LEFT] and floor_map[pl_y][pl_x - 1] != 1:
                pl_x -= 1
            elif keys[K_RIGHT] and floor_map[pl_y][pl_x + 1] != 1:
                pl_x += 1

            # 敵との接触判定
            if floor_map[pl_y][pl_x] == 3:
                idx = 2
                tmr = 0

        elif idx == 2:  # 戦闘画面
            draw_battle(screen, font)
            keys = pygame.key.get_pressed()

            if keys[K_SPACE] and tmr % 10 == 0:  # スペースキーで攻撃
                enemy_life -= random.randint(1, 5)
                if enemy_life <= 0:
                    # 敵を倒したらフロア画面に戻る
                    enemy_life = 10  # 敵のHPをリセット
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
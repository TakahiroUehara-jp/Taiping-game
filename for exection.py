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
pl_y = 9                     #プレイヤーの座標を管理
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
    global stage
    enemy_name = enemies[stage]
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
            elif tile == 3:
                screen.blit(enemy_name, (X, Y))
            # プレイヤーの描画
            if x == pl_x and y == pl_y:
                screen.blit(player, (X, Y))


def main():
    global idx, tmr, pl_x, pl_y, enemy_hp
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
            draw_text(screen, "Press SPACE to Start", 250, 260, font, RED)
            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                idx = 1
                tmr = 0

        elif idx == 1:  # ゲーム画面（フロア探索）
            draw_floor(screen)
            keys = pygame.key.get_pressed()
            if keys[K_UP] and floor_map[pl_y - 1][pl_x] != 1:
                pl_y -= 1
            elif keys[K_DOWN] and floor_map[pl_y + 1][pl_x] != 1:
                pl_y += 1
            elif keys[K_LEFT] and floor_map[pl_y][pl_x - 1] != 1:
                pl_x -= 1
            elif keys[K_RIGHT] and floor_map[pl_y][pl_x + 1] != 1:
                pl_x += 1


        pygame.display.update()
        clock.tick(10)  # 1秒間に10フレーム更新

def draw_text(screen, text, x, y, font, color):
    """テキストの描画"""
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

if __name__ == "__main__":
    main()

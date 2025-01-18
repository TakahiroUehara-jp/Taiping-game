# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:18:42 2025

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

# グローバル変数の初期化
pl_x = 1  # プレイヤーの初期タイルX座標
pl_y = 1  # プレイヤーの初期タイルY座標
idx = 0
tmr = 0

# フロアマップ
floor_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def draw_floor(screen):
    """フロアの描画"""
    for y, row in enumerate(floor_map):
        for x, tile in enumerate(row):
            X = x * 48
            Y = y * 48
            if tile == 0:
                screen.blit(floor, (X, Y))
            elif tile == 1:
                screen.blit(wall, (X, Y))
            elif tile == 2:
                screen.blit(door, (X, Y))
            # プレイヤーの描画
            if x == pl_x and y == pl_y:
                screen.blit(player, (X, Y))

def main():
    global idx, tmr, pl_x, pl_y
    pygame.init()
    pygame.display.set_caption("Typing Game")
    screen = pygame.display.set_mode((432, 336))
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
            screen.blit(title, (10, 5))
            draw_text(screen, "Press SPACE to Start", 100, 200, font, CYAN)
            if pygame.key.get_pressed()[K_SPACE]:
                idx = 1
                tmr = 0

        elif idx == 1:  # ゲーム開始
            draw_floor(screen)
            keys = pygame.key.get_pressed()

            # プレイヤーの移動
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
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
enemy_floor =pygame.image.load("picture\enem lvmax.jpg")

# グローバル変数の初期化
pl_x, pl_y = 1, 1  # プレイヤーの初期タイル座標
idx = 0  # ゲーム状態
tmr = 0  # タイマー
enemy_hp = 10  # 敵のHP

# フロアマップ（0: 床, 1: 壁, 2: ドア, 3: 敵）
floor_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
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
                screen.blit(enemy_floor, (X, Y))
            # プレイヤーの描画
            if x == pl_x and y == pl_y:
                screen.blit(player, (X, Y))

def draw_battle(screen, font):
    """戦闘画面の描画"""
    screen.fill(BLACK)
    draw_text(screen, "戦闘中！", 160, 100, font, WHITE)
    draw_text(screen, f"敵のHP: {enemy_hp}", 160, 150, font, RED)
    draw_text(screen, "スペースキーで攻撃", 100, 250, font, CYAN)

def main():
    global idx, tmr, pl_x, pl_y, enemy_hp
    pygame.init()
    pygame.display.set_caption("Typing Game")
    screen = pygame.display.set_mode((700, 700))
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
            screen.blit(title, (10, 5))
            draw_text(screen, "Press SPACE to Start", 100, 200, font, CYAN)
            if pygame.key.get_pressed()[K_SPACE]:
                idx = 1
                tmr = 0

        elif idx == 1:  # ゲーム画面（フロア探索）
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

            # 敵との接触判定
            if floor_map[pl_y][pl_x] == 3:
                idx = 2
                tmr = 0

        elif idx == 2:  # 戦闘画面
            draw_battle(screen, font)
            keys = pygame.key.get_pressed()

            if keys[K_SPACE] and tmr % 10 == 0:  # スペースキーで攻撃
                enemy_hp -= random.randint(1, 5)
                if enemy_hp <= 0:
                    # 敵を倒したらフロア画面に戻る
                    enemy_hp = 10  # 敵のHPをリセット
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
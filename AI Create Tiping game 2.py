# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:07:38 2025

@author: takau
"""

import pygame
import random

# 初期化
pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("タイピングゲーム")

# 色設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# フォント設定
font = pygame.font.Font(None, 50)

# 単語リスト
words = ["sushi", "tempura", "ramen", "wasabi", "nigiri", "miso", "udon", "sake"]
current_word = random.choice(words)

# ゲームの変数
score = 0
timer = 30
clock = pygame.time.Clock()

# 入力文字列
input_text = ""

# ゲームループ
running = True
while running:
    screen.fill(WHITE)

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                if input_text == current_word:
                    score += 1
                    current_word = random.choice(words)
                input_text = ""
            else:
                input_text += event.unicode

    # タイマーの更新
    timer -= clock.get_time() / 1000
    if timer <= 0:
        running = False

    # テキスト描画
    word_text = font.render(current_word, True, BLACK)
    input_text_render = font.render(input_text, True, RED)
    score_text = font.render(f"Score: {score}", True, BLACK)
    timer_text = font.render(f"Time: {int(timer)}", True, BLACK)

    screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2, HEIGHT // 4))
    screen.blit(input_text_render, (WIDTH // 2 - input_text_render.get_width() // 2, HEIGHT // 2))
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (WIDTH - 150, 10))

    # 画面更新
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

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
# 画像の読み込み
title = pygame.image.load("picture/Tittle Screan(2).png")
player = pygame.image.load("picture/player.png")
wall = pygame.image.load("picture/wall.png")
floor = pygame.image.load("picture/floor.png")
door = pygame.image.load("picture//door.png")
BtlBG = pygame.image.load("picture//btlbg.png")

#戦闘外用の敵の画像
enemy1 = pygame.image.load("picture/enemy lv1.png")
enemy2 = pygame.image.load("picture/enemy lv2.png")
enemy3 = pygame.image.load("picture/enemy lv3.png")
enemy4 = pygame.image.load("picture/enemy lv4.png")
enemy5 = pygame.image.load("picture/enemy lv5.png")

#戦闘内用の敵の画像
Enemy1 = pygame.image.load("picture/enemy lv1 (2).png")
Enemy2 = pygame.image.load("picture/enemy lv2 (2).png")
Enemy3 = pygame.image.load("picture/enemy lv3 (2).png")
Enemy4 = pygame.image.load("picture/enemy lv4 (2).png")
Enemy5 = pygame.image.load("picture/enemy lv5 (2).png")

key1 = pygame.image.load("picture/key1.png")
key2 = pygame.image.load("picture/key2.png")
key3 = pygame.image.load("picture/key3.png")
key4 = pygame.image.load("picture/key4.png")


# グローバル変数の初期化
pl_x, pl_y = 5, 9  # プレイヤーの初期タイル座標
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


enemies = [enemy1,enemy2,enemy3,enemy4,enemy5]
enemy2 = [Enemy1,Enemy2,Enemy3,Enemy4,Enemy5]

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
    global stage
    enemy = enemies[stage]
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
                screen.blit(enemy, (X, Y))
                            
            if x == pl_x and y == pl_y:
                screen.blit(player, (X, Y))

                
def init_battle():
    global emy_name,emy_lifemax,emy_life,emy_x,emy_y,stage
    enemy = enemies[stage]
    
    emy_life = emy_lifemax
    emy_lifemax = stage*100                                                           #仮設定
    emy_name = enemy + "lv" + str(stage)
    emy_x = 440-enemies.get_width()/2
    emy_y = 560-enemies.get_height()
    
def draw_bar(screen, x, y, width, height, current, maximum):                    #draw_barは定義されていなかたので、仮で定義しておきました。細かな調整は後でやってね
    ratio = current / maximum                                                  # ゲージの比率を計算
    
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

def draw_para(screen, font):
    # プレイヤーの能力を表示
    draw_text(screen, f"HP: {pl_life}/{pl_lifemax}", 20, 20, font, WHITE)
    # 必要に応じて、攻撃力や防御力など他の能力を追加
#コメント　draw_paraが定義されていなかったので、定義しました。


def draw_battle(screen, font):
    """戦闘画面の描画"""
    global emy_blink, dmg_eff,enemies,stage
    bx = 0
    by = 0
    if dmg_eff > 0:
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    screen.blit(BtlBG, [bx, by])
    enemy = enemy2[stage]
    screen.blit(enemy, [300, 350])
    draw_bar(screen, 340, 580, 200, 10, emy_life, emy_lifemax)
    if emy_blink > 0:
        emy_blink = emy_blink - 1
    for i in range(10): # 戦闘メッセージの表示
        draw_text(screen, message[i], 600, 100+i*50, font, WHITE)
    draw_para(screen, font) # 主人公の能力を表示

def draw_text(screen, text, x, y, font, color):
    """テキストの描画"""
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))
    
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
    global idx, tmr, pl_x, pl_y,pl_life, enemy_life, dmg
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
            draw_text(screen, "", 230, 350, font, CYAN)
            if pygame.key.get_pressed()[K_SPACE]:
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

            # 敵との接触判定
            if floor_map[pl_y][pl_x] == 3:
                idx = 2
                tmr = 0

        elif idx == 2:  # 戦闘画面
            if tmr == 1:
                draw_battle(screen, font)
                init_battle(screen, font)
                init_message()
                keys = pygame.key.get_pressed()
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
            if keys[K_SPACE] and tmr % 10 == 0:  # スペースキーで攻撃
                enemy_hp -= random.randint(1, 5)
                if enemy_hp <= 0:
                    # 敵を倒したらフロア画面に戻る
                    enemy_hp = 10  # 敵のHPをリセット
                    idx = 1
                    # 敵を消す
                    floor_map[pl_y][pl_x] = 0
        
                
        elif idx == 3:# プレイヤーのターン（入力待ち）
            draw_battle(screen)
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
            draw_battle(screen)
            if tmr == 1:
                dmg = mojisuu                                                #mojisuuはタイピングの記述がないため仮置き
            if 2 <= tmr and tmr <= 4:
                screen.blit(imgEffect[0], [700-tmr*120, -100+tmr*120])
            if tmr == 5:
                emy_blink = 5
                set_message(str(dmg)+"pts of damage!")
            if tmr == 11:
                enemy_life = enemy_life - dmg
                if enemy_life <= 0:
                    enemy_life = 0
                    idx = 6
                    tmr = 0
            if tmr == 16:
                idx = 3
                tmr = 0

        elif idx == 5: # 敵の攻撃
            draw_battle(screen)
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
               keys = keys + 1
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

            
            
        pygame.display.update()
        clock.tick(30)

def main():
    global idx, tmr, pl_x, pl_y, enemy_life,dmg,pl_life
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
                stage = 1
                welcome = 20
                pl_lifemax = 100
                pl_life = pl_lifemax
                idx = 1
                tmr = 0

        elif idx == 1:  # ゲーム画面（フロア探索）
            draw_floor(screen)
            keys = pygame.key.get_pressed()                                    #pygame.key.get_pressedは押されているキーをリアルタイム判定できる関数
            # プレイヤーの移動
            if keys[K_UP] and floor_map[pl_y - 1][pl_x] != 1:
                pl_y -= 1                                                      #プレイヤーがKey_upを押して、フロアの1つ上の座標が1=壁じゃなかったら、そこに移動していいよって指示、下も同じ
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

            if keys[K_SPACE] and tmr % 10 == 0:                                # スペースキーで攻撃
                enemy_hp -= random.randint(1, 5)
                if enemy_hp <= 0:
                    # 敵を倒したらフロア画面に戻る
                    enemy_hp = 10  # 敵のHPをリセット
                    idx = 1
                    # 敵を消す
                    floor_map[pl_y][pl_x] = 0
        
        elif idx == 3:# プレイヤーのターン（入力待ち）
            draw_battle(screen)
            if tmr == 1: 
                set_message("文字を")
            if tmr == 15:
                user_input = entry.get()
                if user_input == "正解":                                        #ここで正解の判定
                    label.config(fg="black")                                   # 文字の色を黒色に変更
                    tmr = 0
                else:
                    label.config(fg="red")                                     # 不正解の場合は赤色に変更
                    tmr = 0

        elif idx == 4: # プレイヤーの攻撃
            draw_battle(screen)
            if tmr == 1:
                dmg = mojisuu
            if 2 <= tmr and tmr <= 4:
                screen.blit(imgEffect[0], [700-tmr*120, -100+tmr*120])
            if tmr == 5:
                emy_blink = 5
                set_message(str(dmg)+"pts of damage!")
            if tmr == 11:
                enemy_life = enemy_life - dmg
                if enemy_life <= 0:
                    enemy_life = 0
                    idx = 6
                    tmr = 0
            if tmr == 16:
                idx = 3
                tmr = 0

        elif idx == 5: # 敵の攻撃
            draw_battle(screen)
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
               keys = keys + 1
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
        clock.tick(10)  # 1秒間に10フレーム更新


if __name__ == "__main__":
    main()

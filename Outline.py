# あらすじテキスト
story_text = [
    "コトバ王国は平和なコトバで満ちあふれ、そこに住む人々はいつも笑顔で平穏な暮らしを送っていた。",
    "しかし100年前に復活した魔王バリーによってコトバ王国は侵略の脅威にさらされていた。",
    "魔王バリーはかつての先代魔王ゾーゴンの封印を解き、完全体としての魔王になり、",
    "勇者コトノハマモルは生まれ育ったコトバ王国を守るため、",
    "魔王討伐を胸に誓い旅立つのであった。"
]

def draw_story(screen, font):
    #あらすじを画面に表示する関数
    screen.fill(BLACK)  # 背景を黒で塗りつぶす色とかはあとで調整
    for i, line in enumerate(story_text):
        draw_text(screen, line, 60, 100 + i * 50, font, WHITE)  # テキストを1行ずつ表示
#大きさとかは仮
def draw_text(screen, txt, x, y, fnt, col):
    #テキストを描画する汎用関数
    sur = fnt.render(txt, True, col)
    screen.blit(sur, [x, y])

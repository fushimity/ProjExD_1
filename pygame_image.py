import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  # 練習1
    kk_img = pg.image.load("fig/3.png")  # 練習3：こうかとん画像の読み込み
    kk_img = pg.transform.flip(kk_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr  # 練習5：背景画像移動用の変数
        screen.blit(bg_img, [-x, 0])  # 練習2
        screen.blit(kk_img, [300, 200])  # 練習4：こうかとんSurfaceの描画
        pg.display.update()
        tmr += 1        
        clock.tick(200)  # 練習6：FPSの変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
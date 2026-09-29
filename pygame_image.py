import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)  # 練習8：左右反転した背景画像Surface
    kk_img = pg.image.load("fig/3.png")  # 練習3：こうかとん画像Surfaceの作成
    kk_img = pg.transform.flip(kk_img, True, False)  # 練習3：こうかとん左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200  # 練習9：ループさせる
        screen.blit(bg_img, [-x, 0])  # 練習5：背景画像を右から左に
        screen.blit(bg_img2, [-x+1600, 0])  # 練習7：2枚目の背景画像
        screen.blit(bg_img, [-x+3200, 0])  # 練習9：3枚目の背景画像
        screen.blit(kk_img, [300, 200])  # 練習4：こうかとんSurfaceを貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(200)  # 練習6：FPS変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
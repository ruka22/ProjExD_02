import pygame as pg
import sys

import random
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1400, 700))  #変更済
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02-20230425/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02-20230425/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0
    #ここまで既存
    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img, (255,0,0), (10,10),10 )  #ex01
    bb_img.set_colorkey((0,0,0))
    x , y = random.randint(0,1400), random.randint(0,700)  #ex02
    screen.blit(bb_img,[x, y])

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
import pygame as pg
import sys

import random

#ex04
delta = {
    pg.K_UP: (0, -1),
    pg.K_DOWN: (0, +1),
    pg.K_LEFT: (-1, 0),
    pg.K_RIGHT: (+1, 0),
    }

#ex05
def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool,bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引数１：画面SurfaceのRect
    引数２：こうかとんor爆弾SurfaceのRect
    戻り値：横、縦方向のはみだし判定結果(画面内→True、画面外→False)
    """

    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))  #変更済
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02-20230425/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02-20230425/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    #ここまで既存
    kk_rct = kk_img.get_rect()  #ex04
    kk_rct.center = 900, 400

    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img, (255,0,0), (10,10),10 )  #ex01
    bb_img.set_colorkey((0,0,0))
    x , y = random.randint(0,1600), random.randint(0,900)  #ex02
    #screen.blit(bb_img,[x, y])
    vx, vy = +1, +1  #ex03
    bb_rct = bb_img.get_rect()
    bb_rct.center = x, y
    #ここから既存
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        #ex04
        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)  #move_ip:移動メソッド(引数：横速度、縦速度)
        #ex05
            if check_bound(screen.get_rect(), kk_rct) != (True, True):
                for k, mv in delta.items():
                    if key_lst[k]:
                        kk_rct.move_ip(-mv[0], -mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)  #ex04改変
        bb_rct.move_ip(vx,vy)  #ex03
        screen.blit(bb_img, bb_rct)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
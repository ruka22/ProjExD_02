import pygame as pg
import sys

import random

#ex04
#追加(斜め移動)
delta = {
    pg.K_r: (0, -1),  #上
    pg.K_v: (0, +1),  #下
    pg.K_d: (-1, 0),  #左
    pg.K_g: (+1, 0),  #右
    pg.K_t: (+1, -1),  #右上
    pg.K_b: (+1, +1),  #右下
    pg.K_e: (-1, -1),  #左上
    pg.K_c: (-1, +1)  #左下
    }

kk_img = pg.image.load("ex02/fig/3.png")
    #kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)  #引数：(角度、拡大)
    #追加１(途中)
    #kk_img = pg.transform.rotozoom(kk_img, 45, 2.0)
kk_imgs = {(0, -1):pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 90, 2.0),
            (+1, -1):pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 45, 2.0),
            (+1, 0):pg.transform.flip(kk_img, True, False),
            (+1, +1):pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 315, 2.0),
            (0, +1):pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 270, 2.0),
            (-1, +1):pg.transform.rotozoom(kk_img, 45, 2.0),
            (-1, 0):pg.transform.rotozoom(kk_img, 0, 2.0),
            (-1, -1):pg.transform.rotozoom(kk_img, 315, 2.0)}

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
    screen = pg.display.set_mode((1600,900))  #変更済
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    
    #追加２
    accs = [a for a in range(1,11)]
    #for r in range(1,11):
    #    bb_img = pg.Surface((20*r, 20*r))
    #    pg.draw.circle(bb_img, (255,0,0), (10*r, 10*r), 10*r)
    #    bb_imgs.append(bb_img)
    kk_rct = kk_img.get_rect()  #ex04
    kk_rct.center = 900, 400

    bb_img = pg.Surface((20,20))
    di = 10
    pg.draw.circle(bb_img, (255,0,0), (10,10), di)  #ex01
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
                font = pg.font.Font(None,80)
                txt = fonto.render("Game Over", True,(255, 255, 255))
                screen.blit(txt, [800, 450])
                return 0

        tmr += 1
        
        #ex04
        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)  #move_ip:移動メソッド(引数：横速度、縦速度)
        #ex05
            if check_bound(screen.get_rect(), kk_rct) != (True, True):
                for k, mv in delta.items():  #mv:移動タプル
                    if key_lst[k]:
                        kk_rct.move_ip(-mv[0], -mv[1])

        #追加２的な
        if tmr % 100 == 0:
            vx, vy = accs[random.randint(0,9)], accs[random.randint(0,9)]

        screen.blit(bg_img, [0, 0])
        #screen.blit(kk_img, kk_rct)  #ex04改変
        screen.blit(kk_imgs[mv], kk_rct)
        bb_rct.move_ip(vx,vy)  #ex03
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko: #横に出てる
            vx *= -1
        if not tate:  #縦に出てる
            vy *= -1
        screen.blit(bb_img, bb_rct)
        if kk_rct.colliderect(bb_rct):  #ex06
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
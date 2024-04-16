import os
import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    
    # 初期化 #
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
        # 変数 #
    background_img = pg.image.load("fig/pg_bg.jpg")
    background_x = 0
    player = pg.image.load("fig/3.png")
    player = pg.transform.flip(player,True,False)
    player_rect = player.get_rect()
    player_rect.center = 300,200
    tmr = 0
    
    while True:
        pressed_keys =pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(background_img,[background_x*-1,0])
        screen.blit(background_img,[background_x*-1+1600,0])
        screen.blit(player,player_rect)

        # 変数
        if pressed_keys[pg.K_UP]:
            player_rect.move_ip(0,-2)
        elif pressed_keys[pg.K_DOWN]:
            player_rect.move_ip(0,2)
        elif pressed_keys[pg.K_LEFT]:
            player_rect.move_ip(-2,0)
        elif pressed_keys[pg.K_RIGHT]:
            player_rect.move_ip(2,0)
            background_x += 1
        if not pressed_keys[pg.K_LEFT]:
            player_rect.move_ip(-1,0)
        background_x = (background_x + 1) % 1600
        tmr += 1

        # 更新
        pg.display.update()
        clock.tick(200)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pg.init()
    main()
    pg.quit()
    sys.exit()
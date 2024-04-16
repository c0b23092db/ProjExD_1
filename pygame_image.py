import os
import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    background_img = pg.image.load("fig/pg_bg.jpg")
    player = pg.image.load("fig/3.png")
    player = pg.transform.flip(player,True,False)
    player_rect = player.get_rect()
    player_rect.center = 300,200
    tmr = 0
    background_x = 0
    clock  = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(background_img,[background_x*-1,0])
        screen.blit(background_img,[background_x*-1+1600,0])
        background_x = (background_x + 2) % 1600
        screen.blit(player,player_rect)
        pressed_keys =pg.key.get_pressed()
        if pressed_keys[pg.K_UP]:
            player_rect.move_ip(0,-1)
        elif pressed_keys[pg.K_DOWN]:
            player_rect.move_ip(0,1)
        elif pressed_keys[pg.K_LEFT]:
            player_rect.move_ip(-1,0)
        elif pressed_keys[pg.K_RIGHT]:
            player_rect.move_ip(1,0)
        pg.display.update()
        tmr += 1
        clock.tick(200)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pg.init()
    main()
    pg.quit()
    sys.exit()
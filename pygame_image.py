import os
import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    background_img = pg.image.load("fig/pg_bg.jpg")
    player_img = pg.image.load("fig/3.png")
    player_img = pg.transform.flip(player_img,True,False)
    clock  = pg.time.Clock()
    tmr = 0
    background_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(background_img,[background_x*-1,0])
        screen.blit(background_img,[background_x*-1+1600,0])
        background_x = (background_x + 2) % 1600
        screen.blit(player_img,[300,200])
        print(background_x)
        pg.display.update()
        tmr += 1
        clock.tick(200)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pg.init()
    main()
    pg.quit()
    sys.exit()
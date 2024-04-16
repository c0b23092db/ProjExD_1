import os
import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    background_img = pg.image.load("fig/pg_bg.jpg")
    player = pg.Surface((25,25))
    player_img = pg.image.load("fig/3.png")
    player_img = pg.transform.flip(player_img,True,False)
    clock  = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(background_img, [0, 0])
        screen.blit(player_img,[300,200])
        pg.display.update()
        tmr += 1
        clock.tick(200)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pg.init()
    main()
    pg.quit()
    sys.exit()
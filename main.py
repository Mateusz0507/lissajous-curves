import pygame as pg
from sys import exit
from functions import (
    initialize_circles,
    update_points_on_circles,
    draw,
    is_reset,
    reset,
)
from constants import WINDOW_SIZE, FPS, N


def main():
    pg.init()
    pg.display.set_caption("Lissajous curves")
    WINDOW = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pause_mode = False

    circles_x, circles_y = initialize_circles()
    curves = [[[] for x in range(N)] for y in range(N)]

    ticks = 0
    while True:
        pg.time.Clock().tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
                elif event.key == pg.K_SPACE:
                    pause_mode = not pause_mode

        if not pause_mode:
            update_points_on_circles(circles_x, circles_y, ticks)
            draw(WINDOW, circles_x, circles_y, curves)
            ticks += 1

            if is_reset(ticks):
                ticks, curves = reset()


if __name__ == "__main__":
    main()

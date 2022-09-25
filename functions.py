import pygame as pg
from constants import RADIUS, SPACING, FPS, N, T
from Circle import Circle
from constants import WINDOW_SIZE
from colors import WHITE, BLACK, CURVES_COLORS


def initialize_circles():
    circles_x = [
        Circle((i + 2) * SPACING + (3 + 2 * i) * RADIUS, SPACING + RADIUS, i + 1)
        for i in range(N)
    ]
    circles_y = [
        Circle(SPACING + RADIUS, (i + 2) * SPACING + (3 + 2 * i) * RADIUS, i + 1)
        for i in range(N)
    ]
    return circles_x, circles_y


def update_points_on_circles(circles_x, circles_y, time):
    for circle in circles_x:
        circle.update_point(time)
    for circle in circles_y:
        circle.update_point(time)


def draw(surface, circles_x, circles_y, curves):
    surface.fill(BLACK)
    # Draw curves
    for x in range(N):
        for y in range(N):
            curves[y][x].append([circles_x[x].point_x, circles_y[y].point_y])
            if len(curves[y][x]) > 1:
                pg.draw.lines(surface, CURVES_COLORS[y], False, curves[y][x], 3)
                pg.draw.circle(surface, WHITE, curves[y][x][-1], 4)
    # Draw circles and lines
    for circle in circles_x:
        circle.draw(surface)
        pg.draw.line(surface, WHITE, (circle.point_x, 0), (circle.point_x, WINDOW_SIZE))
    for circle in circles_y:
        circle.draw(surface)
        pg.draw.line(surface, WHITE, (0, circle.point_y), (WINDOW_SIZE, circle.point_y))

    pg.display.update()


def is_reset(time):
    return time >= T * FPS


def reset():
    return 0, [[[] for x in range(N)] for y in range(N)]

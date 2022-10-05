import pygame as pg
import ctypes


ctypes.windll.user32.SetProcessDPIAware()
pg.init()

# INCREASING N OR FPS CAN DICREASE PERMORMANCE
# Number of leading circles (MAX 9)
# Total number of curves: N^2
N = 9

FPS = 60

# Lap time of point with speed = 1 (in seconds)
T = 4

# Radius of circles (in pixels)
RADIUS = 40

# Spacing between circles (in pixels)
SPACING = 15

WINDOW_SIZE = 2 * (N + 1) * RADIUS + (N + 2) * SPACING

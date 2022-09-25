import pygame as pg
from math import pi, sin, cos
from constants import RADIUS, FPS, T
from colors import WHITE


class Circle:
    def __init__(self, x, y, speed_of_point):
        self.x = x
        self.y = y
        self.speed_of_point = speed_of_point
        self.r = RADIUS
        self.color = WHITE
        self.angle = 0
        self.point_x = 0
        self.point_y = 0

    def update_point(self, time):
        self.angle = time * self.speed_of_point * 2 * pi / (T * FPS)
        self.point_x = self.x + self.r * cos(self.angle)
        self.point_y = self.y - self.r * sin(self.angle)

    def draw(self, surface):
        pg.draw.circle(surface, WHITE, (self.x, self.y), self.r, 1)
        pg.draw.circle(surface, WHITE, (self.point_x, self.point_y), 7)

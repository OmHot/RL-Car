import numpy as np
import pygame as pg
from random import randint
from pygame.math import Vector2
from math import sqrt, sin, cos, radians, degrees, copysign,atan2
__all__ = "NPC"

class NPC:
    """Kinematic model of a car with radars for calculating distances to objects"""

    def __init__(self, spawn_position=(0.0, 0.0), spawn_angle=0, scale=1,
                 show_collision=True, show_radars=True, show_score=False):
        sprite = pg.image.load(f"autopilot/sprites/car{randint(0, 63)}.png")
        rect = sprite.get_rect()
        w, h = round(rect.width * scale), round(rect.height * scale)
        self.car_sprite = pg.transform.scale(sprite, (w, h))
        self.car_sprite_width = 0.5 * w - 5
        self.car_sprite_height = 0.5 * h - 10
        self.chassis_length = 0.03 * h

        self.angle = spawn_angle
        self.position = Vector2(*spawn_position)#Position 
        self.velocity = Vector2(0.0, 0.0)
        self.acceleration = 0.0
        self.steering = 0.0

        self.max_velocity = 100.0 * scale
        self.max_acceleration = 3.0 * scale
        self.max_steering = 1.5 * scale
        self.max_radar_len = int(300 * scale)

        self.show_collision_points = show_collision
        self.show_radars = show_radars
        self.show_score = show_score
    def translate(self,nextpos):
        x1, y1 = self.position
        x2, y2 = nextpos

        dx = x2 - x1
        dy = y2 - y1

        self.angle = -degrees(atan2(dy,dx))
        self.position = nextpos

    def draw(self, screen):
        """Renders a car model with radars and collision points"""
        rotated = pg.transform.rotate(self.car_sprite, self.angle)
        rect = rotated.get_rect()
        screen.blit(rotated, self.position - Vector2(rect.width / 2, rect.height / 2))

        """if self.show_score:
            font = pg.font.SysFont("Comic Sans MS", int(20 * self.scale))
            label = font.render(str(round(self.score)), True, (0, 0, 0))
            label_rect = label.get_rect()
            label_rect.center = self.position
            screen.blit(label, label_rect)"""
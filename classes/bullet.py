# Standard Library Imports

# Third Party Imports
import pygame

# Local Application Imports
from classes.baseobject import BaseObject


class Bullet(BaseObject):

    IMG = pygame.image.load("./images/bullet.png")
    BULLET_READY = "ready"
    BULLET_FIRE = "fire"
    ON_SCREEN = False

    # ready -- state meaning, cannot see bullet on screen
    # fire -- state meaning, bullet is currently moving on screen
    bullet_state = BULLET_READY

    def __init__(self, player):
        super().__init__(player.x_cord + 16, player.y_cord)
        self.y_change = 1

    @classmethod
    def reset_bullet_state(cls):

        cls.bullet_state = cls.BULLET_READY
        cls.ON_SCREEN = False

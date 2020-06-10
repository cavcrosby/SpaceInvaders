# Standard Library Imports

# Third Party Imports
import pygame

# Local Application Imports
from classes.baseobject import BaseObject


class Bullet(BaseObject):

    IMG = pygame.image.load("./images/bullet.png")
    BULLET_READY = "ready"
    BULLET_FIRE = "fire"

    # ready -- state meaning, cannot see bullet on screen
    # fire -- state meaning, bullet is currently moving on screen
    bullet_state = BULLET_READY

    def __init__(self, player):

        super().__init__(x_cord=player.x_cord + 16, y_cord=player.y_cord)
        self.y_change = 1

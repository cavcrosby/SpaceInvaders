# Standard Library Imports
import random

# Third Party Imports
import pygame

# Local Application Imports
from classes.baseobject import BaseObject


class Enemy(BaseObject):

    IMG = pygame.transform.scale(
        pygame.image.load("./images/alien.png"), (56, 56)
    )
    IMG_WIDTH = IMG.get_rect().size[0]

    def __init__(self, screen_boundary_x):
        super().__init__(
            x_cord=random.randint(0, screen_boundary_x - self.IMG_WIDTH),
            y_cord=random.randint(50, 100),
        )
        self.x_cord_change = 0.5
        self.y_cord_change = 20

    @classmethod
    def from_manual_cords(cls, x_cord, y_cord, x_cord_change, y_cord_change):
        """Generate an enemy at given coordinates with change.

        Examples
        ------
        >>> enemies = [Enemy.from_manual_cords(500, 470, 0.2, 0)]

        """
        enemy = cls(cls.IMG_WIDTH)
        enemy.x_cord = x_cord
        enemy.y_cord = y_cord
        enemy.x_cord_change = x_cord_change
        enemy.y_cord_change = y_cord_change
        return enemy

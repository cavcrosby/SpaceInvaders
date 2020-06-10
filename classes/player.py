# Standard Library Imports

# Third Party Imports
import pygame

# Local Application Imports
from classes.baseobject import BaseObject


class Player(BaseObject):
    IMG = pygame.transform.scale(
        pygame.image.load("./images/player_ship.png"), (56, 56)
    )
    IMG_WIDTH = IMG.get_rect().size[0]

    def __init__(self):

        super().__init__(x_cord=370, y_cord=480)
        self.x_cord_change = 0

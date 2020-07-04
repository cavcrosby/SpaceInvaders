# Standard Library Imports
import random
from abc import ABC, abstractproperty

# Third Party Imports
import pygame
import pygame.mixer

# Local Application Imports
from configurations import (
    DEFAULT_ENEMY_DROP,
    DEFAULT_ENEMY_SPEED,
    BULLET_SHOOTING_SOUND_PATH,
    NOT_INITIALIZED,
    OFF_SCREEN_Y_CORD,
    SCREEN_BOUNDARY_Y,
    SCREEN_BOUNDARY_X,
)


class GameObject(ABC):
    @abstractproperty
    def IMG(self):

        NotImplemented

    @property
    def NO_IMG(self):

        return None

    def __init_subclass__(cls, *args, **kwargs):
        """Specifications required by future SpaceInvader subclasses."""
        super().__init_subclass__(*args, **kwargs)

        if cls.IMG is NotImplemented:
            raise NotImplementedError(
                f"Error: IMG not implemented in {cls.__name__}"
            )

    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def blit(self, screen):
        if self.IMG == self.NO_IMG:
            raise ValueError(
                f"No image is set for the {type(self).__name__} object!"
            )
        screen.blit(self.IMG, (self.x_cord, self.y_cord))


class Player(GameObject):

    IMG = pygame.transform.scale(
        pygame.image.load("./images/player_ship.png"), (56, 56)
    )
    IMG_WIDTH = IMG.get_rect().size[0]
    X_UPPER_BOUNDARY = SCREEN_BOUNDARY_X - IMG_WIDTH
    bullet = NOT_INITIALIZED

    def __init__(self):

        super().__init__(x_cord=370, y_cord=480)
        self.x_cord_change = 0

    def bullet_init(self):

        bullet = Bullet(self, y_change=1, x_offset=20)
        bullet_sound = pygame.mixer.Sound(BULLET_SHOOTING_SOUND_PATH)
        bullet_sound.play()
        self.bullet = bullet

    def reset_bullet(self):

        self.bullet.reset_bullet()
        self.bullet = NOT_INITIALIZED


class Enemy(GameObject):

    IMG = pygame.transform.scale(
        pygame.image.load("./images/alien.png"), (56, 56)
    )
    IMG_WIDTH = IMG.get_rect().size[0]
    X_UPPER_BOUNDARY = SCREEN_BOUNDARY_X - IMG_WIDTH

    def __init__(self, screen_boundary_x):
        super().__init__(
            x_cord=random.randint(0, screen_boundary_x - self.IMG_WIDTH),
            y_cord=random.randint(50, 100),
        )
        self.x_cord_change = DEFAULT_ENEMY_SPEED
        self.y_cord_change = DEFAULT_ENEMY_DROP

    def bullet_init(self):

        bullet = Bullet(self, y_change=-1, x_offset=22, y_offset=20)
        return bullet

    def reset_bullet(self):

        self.bullet = NOT_INITIALIZED

    @classmethod
    def from_manual_cords(
        cls,
        x_cord,
        y_cord,
        x_cord_change=DEFAULT_ENEMY_SPEED,
        y_cord_change=DEFAULT_ENEMY_DROP,
    ):
        """Generate an enemy at given coordinates with change.

        Examples
        ------
        >>> enemies = [Enemy.from_manual_cords(500, 470, 0.2, 0)]

        """
        enemy = cls(cls.IMG_WIDTH)
        enemy.x_cord = x_cord
        enemy.y_cord = y_cord
        if x_cord_change is not DEFAULT_ENEMY_SPEED:
            enemy.x_cord_change = x_cord_change
        if y_cord_change is not DEFAULT_ENEMY_DROP:
            enemy.y_cord_change = y_cord_change
        return enemy


class Bullet(GameObject):

    IMG = pygame.image.load("./images/bullet.png")

    def __init__(self, gameobject, y_change, x_offset=0, y_offset=0):
        super().__init__(
            gameobject.x_cord + x_offset, gameobject.y_cord + y_offset
        )
        self.y_change = y_change

    def is_off_screen(self):

        return self.y_cord < 0 or self.y_cord > SCREEN_BOUNDARY_Y

    def reset_bullet(self):

        self.y_cord = OFF_SCREEN_Y_CORD


class Score(GameObject):

    IMG = GameObject.NO_IMG

    def __init__(self):

        super().__init__(x_cord=10, y_cord=10)
        self.value = 0

    def add_points(self, points):

        if points >= 0:
            self.value += points

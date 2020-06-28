# Standard Library Imports
import os
from os.path import join

# Third Party Imports

# Local Application Imports

PWD = os.getcwd()

# Colors

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

# Configurations (expected to change frequently)

NUMBER_OF_ENEMIES = 12
POINTS_PER_KILL = 20
NUMBER_OF_BLOCKS = 5
DEFAULT_ENEMY_SPEED = 0.12
DEFAULT_ENEMY_DROP = 20

# Configurations (NOT expected to change frequently)

SCREEN_BOUNDARY_X = 800
SCREEN_BOUNDARY_Y = 600
DISPLAY_CAPTION = "Space Invaders"
IMAGES_DIRECTORY_NAME = "images"
MUSIC_DIRECTORY_NAME = "music"
ICON_PATH = join(PWD, "images", "ufo.png")
BACKGROUND_MUSIC_PATH = join(PWD, MUSIC_DIRECTORY_NAME, "background.wav")
BULLET_SHOOTING_SOUND_PATH = join(PWD, MUSIC_DIRECTORY_NAME, "laser.wav")
EXPLOSION_SOUND_PATH = join(PWD, MUSIC_DIRECTORY_NAME, "explosion.wav")
BULLET_SHOOTING_SOUND_PATH = join(PWD, MUSIC_DIRECTORY_NAME, "laser.wav")
GAME_FONT = "freesansbold.ttf"

# Other
OFF_SCREEN = -1
X_LOWER_BOUNDARY = 0
Y_LOWER_BOUNDARY = 0
NOT_INITIALIZED = None

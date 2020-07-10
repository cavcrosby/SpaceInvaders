# Standard Library Imports
from os.path import join

# Third Party Imports

# Local Application Imports

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

POINTS_PER_KILL = 20
NUMBER_OF_BLOCKS = 5
DEFAULT_PLAYER_SPEED = 0.55  # speed on the x-axis
DEFAULT_ENEMY_SPEED = 0.12  # speed on the x-axis
DEFAULT_ENEMY_DROP = 20  # each drop on the y-axis

# Configurations (NOT expected to change frequently)

SCREEN_BOUNDARY_X = 800
SCREEN_BOUNDARY_Y = 600
DISPLAY_CAPTION = "Space Invaders"
ASSETS_DIRECTORY_NAME = "assets"
IMAGES_DIRECTORY_NAME = "images"
IMAGES_DIRECTORY_PATH = join(ASSETS_DIRECTORY_NAME, "images")
FONTS_DIRECTORY_NAME = "fonts"
FONTS_DIRECTORY_PATH = join(ASSETS_DIRECTORY_NAME, "fonts")
MUSIC_DIRECTORY_NAME = "music"
MUSIC_DIRECTORY_PATH = join(ASSETS_DIRECTORY_NAME, "music")
ICON_PATH = join(IMAGES_DIRECTORY_PATH, "ufo.png")
BACKGROUND_MUSIC_PATH = join(MUSIC_DIRECTORY_PATH, "background.wav")
BULLET_SHOOTING_SOUND_PATH = join(MUSIC_DIRECTORY_PATH, "laser.wav")
EXPLOSION_SOUND_PATH = join(MUSIC_DIRECTORY_PATH, "explosion.wav")
BULLET_SHOOTING_SOUND_PATH = join(MUSIC_DIRECTORY_PATH, "laser.wav")
PLAYER_ICON_PATH = join(IMAGES_DIRECTORY_PATH, "player_ship.png")
ENEMY_ICON_PATH = join(IMAGES_DIRECTORY_PATH, "alien.png")
BULLET_ICON_PATH = join(IMAGES_DIRECTORY_PATH, "bullet.png")
GAME_FONT = join(FONTS_DIRECTORY_PATH, "freesansbold.ttf")

# Other

OFF_SCREEN_Y_CORD = SCREEN_BOUNDARY_Y * -5
X_LOWER_BOUNDARY = 0
Y_LOWER_BOUNDARY = 0
NOT_INITIALIZED = None

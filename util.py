# Standard Library Imports
import math

# Third Party Imports
import pygame

# Local Application Imports
from classes.block import Block

GAME_FONT = "freesansbold.ttf"


def show_score(score, screen):

    font = pygame.font.Font(GAME_FONT, 32)
    score_text = font.render("Score: " + str(score.value), True, (255, 255, 255))
    screen.blit(score_text, (score.x_cord, score.y_cord))


def game_over_text(screen):

    font = pygame.font.Font(GAME_FONT, 64)
    text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(text, (200, 250))


def draw_baseobject(obj, screen):

    screen.blit(obj.IMG, (obj.x_cord, obj.y_cord))


def draw_block(screen, block):

    for rect in block.STRUCTURE:
        pygame.draw.rect(screen, (0, 0, 0), rect)


def create_blocks(number_of_blocks):

    blocks = []
    STARTING_X_RANGE = 0
    ENDING_X_RANGE = 800  # TODO ADD SCREEN'S X CORD?
    BLOCK_WIDTH = 90
    DISTANCE_BETWEEN_TOP_LEFT_BLOCKS = 150
    DISTANCE_BETWEEN_BLOCKS = DISTANCE_BETWEEN_TOP_LEFT_BLOCKS - BLOCK_WIDTH
    # [DISTANCE_BETWEEN_BLOCKS] is just the 'empty' space between blocks.

    BLOCK_HEIGHT_TOP = 375
    BLOCK_HEIGHT_BOTTOM = 460
    TOTAL_WIDTH = (BLOCK_WIDTH * number_of_blocks) + (
        DISTANCE_BETWEEN_BLOCKS * (number_of_blocks - 1)
    )
    # [TOTAL_WIDTH] This is the range that the blocks and their distances.

    BLOCKS_X_RANGE = ENDING_X_RANGE - STARTING_X_RANGE
    # [BLOCKS_X_RANGE] This is the range that the blocks and
    # their distances can take up.

    TOP_LEFT_START = (BLOCKS_X_RANGE - TOTAL_WIDTH) / 2

    for i in range(number_of_blocks):

        block = Block(
            top_left=(TOP_LEFT_START, BLOCK_HEIGHT_TOP),
            bottom_right=(TOP_LEFT_START + BLOCK_WIDTH, BLOCK_HEIGHT_BOTTOM),
        )
        TOP_LEFT_START += DISTANCE_BETWEEN_TOP_LEFT_BLOCKS
        blocks.append(block)

    return blocks


def is_collision(x1, x2, y1, y2):

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance < 27:
        return True
    return False

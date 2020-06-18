# Standard Library Imports
import math

# Third Party Imports
import pygame

# Local Application Imports

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


def is_collision(x1, x2, y1, y2):

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance < 27:
        return True
    return False

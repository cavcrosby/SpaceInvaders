# Standard Library Imports
import math

# Third Party Imports
import pygame
from pygame import mixer

# Local Application Imports
from classes.bullet import Bullet


def show_score(score, screen):
    font = pygame.font.Font("freesansbold.ttf", 32)
    score_text = font.render("Score: " + str(score.value), True, (255, 255, 255))
    screen.blit(score_text, (score.x_cord, score.y_cord))


def game_over_text(screen):
    font = pygame.font.Font("freesansbold.ttf", 64)
    text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(text, (200, 250))


def draw_baseobject(obj, screen):
    screen.blit(obj.IMG, (obj.x_cord, obj.y_cord))


def draw_block(screen, block):

    for rect in block.STRUCTURE:
        pygame.draw.rect(screen, (0, 0, 0), rect)


def fire_bullet(bullet, screen):
    Bullet.bullet_state = Bullet.BULLET_FIRE
    draw_baseobject(bullet, screen)


def is_collision(x1, x2, y1, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance < 27:
        return True
    return False

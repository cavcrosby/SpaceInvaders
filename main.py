#!/usr/bin/env python3
# Standard Library Imports

# Third Party Imports
import pygame
from pygame import mixer

# Local Application Imports
import util
import game_logic
from classes.player import Player
from classes.enemy import Enemy
from classes.bullet import Bullet
from classes.score import Score
from classes.block import Block

pygame.init()

# Configurations (expected to change frequently)

SCREEN_BOUNDARY_X = 800
SCREEN_BOUNDARY_Y = 600
NUMBER_OF_ENEMIES = 12
POINTS_PER_KILL = 20

# Configurations (NOT expected to change frequently)

SCREEN_OUT_OF_BOUNDS_Y = SCREEN_BOUNDARY_Y * 5
DISPLAY_CAPTION = "Space Invaders"
ICON_PATH = "./images/ufo.png"
BACKGROUND_MUSIC_PATH = "./music/background.wav"
BULLET_SHOOTING_SOUND_PATH = "./music/laser.wav"
EXPLOSION_SOUND_PATH = "./music/explosion.wav"
NOT_INITIALIZED = None

# In-game configurations
X_UPPER_BOUNDARY_PLAYER = NOT_INITIALIZED
X_UPPER_BOUNDARY_ENEMY = NOT_INITIALIZED
X_LOWER_BOUNDARY = 0
Y_LOWER_BOUNDARY = 0

# Creates the screen
screen = pygame.display.set_mode((SCREEN_BOUNDARY_X, SCREEN_BOUNDARY_Y))

# Caption
pygame.display.set_caption(DISPLAY_CAPTION)

# Icon
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)

# Sound
mixer.music.load(BACKGROUND_MUSIC_PATH)
mixer.music.play(-1)

# Main game objects
score = Score()
player = NOT_INITIALIZED
enemies = NOT_INITIALIZED
bullet = NOT_INITIALIZED

# Blocks, or barriers
block1 = Block(top_left=(125, 350), bottom_right=(175, 400))
block2 = Block(top_left=(275, 350), bottom_right=(325, 400))
block3 = Block(top_left=(425, 350), bottom_right=(475, 400))
block4 = Block(top_left=(575, 350), bottom_right=(625, 400))
blocks = [block1, block2, block3, block4]


def main():

    global bullet
    # Game Loop
    running = True
    game_over = False

    while running:

        # RGB
        screen.fill((0, 180, 0))
        running = game_logic.check_events(player, bullet)

        # bullet Movement
        if Bullet.bullet_state is Bullet.BULLET_FIRE:
            if not Bullet.ON_SCREEN:
                bullet = game_logic.bullet_init(player)
            if bullet.y_cord < Y_LOWER_BOUNDARY:
                game_logic.reset_bullet()
            else:
                util.draw_baseobject(bullet, screen)
                bullet.y_cord -= bullet.y_change
                game_logic.check_block_bullet_collisions(bullet, blocks)

        game_logic.draw_blocks(screen, blocks)

        # player movement
        # player should be stopped on the x axis when the icon_width + position are about to
        # go out of the upper or lower x boundary
        if (player.x_cord + player.x_cord_change < X_LOWER_BOUNDARY) or (
            player.x_cord + player.x_cord_change > X_UPPER_BOUNDARY_PLAYER
        ):
            player.x_cord_change = 0

        # enemy movement
        # enemy should be stopped on the x axis when the icon_width + position are about to
        # go out of the upper or lower x boundary
        for enemy in enemies:
            bullet_enemy_collision = game_logic.check_enemy_bullet_collisions(
                bullet, enemy,
            )
            player_enemy_collision = util.is_collision(
                enemy.x_cord, player.x_cord, enemy.y_cord, player.y_cord,
            )
            if player_enemy_collision or game_over:
                game_logic.do_game_over(enemies, screen)
                game_over = True
                break
            if bullet_enemy_collision:
                game_logic.destroy_enemy(bullet, enemy, enemies, score)
            elif enemy.x_cord + enemy.x_cord_change < X_LOWER_BOUNDARY:
                game_logic.go_down_right(enemy)
            elif enemy.x_cord + enemy.x_cord_change > X_UPPER_BOUNDARY_ENEMY:
                game_logic.go_down_left(enemy)
            enemy.x_cord += enemy.x_cord_change
            util.draw_baseobject(enemy, screen)

        player.x_cord += player.x_cord_change
        util.draw_baseobject(player, screen)
        util.show_score(score, screen)
        pygame.display.update()


def game_init():
    global player
    global enemies
    global X_UPPER_BOUNDARY_PLAYER
    global X_UPPER_BOUNDARY_ENEMY
    player = Player()
    enemies = [Enemy(SCREEN_BOUNDARY_X) for i in range(NUMBER_OF_ENEMIES)]
    X_UPPER_BOUNDARY_PLAYER = SCREEN_BOUNDARY_X - player.IMG_WIDTH
    X_UPPER_BOUNDARY_ENEMY = (
        SCREEN_BOUNDARY_X - enemies[0].IMG_WIDTH
    )  # assuming all enemies use same image


if __name__ == "__main__":
    game_init()
    main()

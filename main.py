#!/usr/bin/env python3
# Standard Library Imports

# Third Party Imports
import pygame
import random
from pygame import mixer

# Local Application Imports
import core
import configurations
from classes.gameobject import (
    Player,
    Enemy,
    Bullet,
    Score,
)

pygame.init()

# Creates the screen
screen = pygame.display.set_mode(
    (configurations.SCREEN_BOUNDARY_X, configurations.SCREEN_BOUNDARY_Y)
)

# Caption
pygame.display.set_caption(configurations.DISPLAY_CAPTION)

# Icon
icon = pygame.image.load(configurations.ICON_PATH)
pygame.display.set_icon(icon)

# Sound
mixer.music.load(configurations.BACKGROUND_MUSIC_PATH)
mixer.music.play(-1)

# In-game configurations
X_UPPER_BOUNDARY_PLAYER = configurations.NOT_INITIALIZED
X_UPPER_BOUNDARY_ENEMY = configurations.NOT_INITIALIZED

# Main game objects
score = Score()
player = configurations.NOT_INITIALIZED
enemy_block = configurations.NOT_INITIALIZED
enemies = configurations.NOT_INITIALIZED
bullet = configurations.NOT_INITIALIZED

# Blocks, or barriers
blocks = core.create_blocks(configurations.NUMBER_OF_BLOCKS)


def main():

    global bullet
    global enemy_block
    # Game Loop
    running = True
    game_over = False

    while running:

        # RGB
        screen.fill((0, 180, 0))
        running = core.check_events(player, bullet)

        # bullet movement
        if Bullet.bullet_state is Bullet.BULLET_FIRE:
            if not Bullet.ON_SCREEN:
                bullet = core.bullet_init(player)
            if bullet.y_cord is configurations.OFF_SCREEN:
                Bullet.reset_bullet_state()
            else:
                bullet.blit(screen)
                bullet.y_cord -= bullet.y_change
                bullet_block_collision = False
                bullet_block_collision = core.is_block_bullet_collision(
                    blocks, bullet
                )
                if bullet_block_collision is not None:
                    core.react_block_bullet_collision(
                        bullet_block_collision["block"],
                        bullet,
                        bullet_block_collision["rect"],
                    )

        for block in blocks:
            block.blit(screen, configurations.BLACK)

        # player movement
        # player should be stopped on the x axis when the icon_width + position
        # are about to go out of the upper or lower x boundary
        if (
            player.x_cord + player.x_cord_change
            < configurations.X_LOWER_BOUNDARY
        ) or (player.x_cord + player.x_cord_change > X_UPPER_BOUNDARY_PLAYER):
            player.x_cord_change = 0

        # enemy movement
        # enemy should be stopped on the x axis when the icon_width + position
        # are about to go out of the upper or lower x boundary
        for enemy in enemies:
            bullet_enemy_collision = (
                core.is_collision(
                    enemy.x_cord, bullet.x_cord, enemy.y_cord, bullet.y_cord
                )
                if Bullet.bullet_state is Bullet.BULLET_FIRE
                else False
            )
            player_enemy_collision = core.is_collision(
                player.x_cord, enemy.x_cord, player.y_cord, enemy.y_cord
            )
            if player_enemy_collision or game_over:
                core.do_game_over(enemies, screen)
                game_over = True
                break
            if bullet_enemy_collision:
                core.destroy_enemy(bullet, enemy, enemies, score)
                continue
            elif (
                enemy.x_cord + enemy.x_cord_change
                < configurations.X_LOWER_BOUNDARY
            ):
                core.go_down_right(enemies, screen)
                break
            elif enemy.x_cord + enemy.x_cord_change > X_UPPER_BOUNDARY_ENEMY:
                core.go_down_left(enemies, screen)
                break
            enemy.blit(screen)
            enemy.x_cord += enemy.x_cord_change

        # choice = random.randint(0, 3)
        # fire_chance = random.randint(1, 5)
        # bottom_enemy = enemy_block.STRUCTURE[choice][-1]
        # if(fire_chance in (1, 2)):
        #     enemy_fire()
            
        if(len(enemies) == 0):
            core.do_game_over(enemies, screen)
        player.blit(screen)
        player.x_cord += player.x_cord_change
        core.show_score(score, screen)
        pygame.display.update()


def game_init():

    global player
    global enemies
    global X_UPPER_BOUNDARY_PLAYER
    global X_UPPER_BOUNDARY_ENEMY
    global enemy_block
    player = Player()
    enemy_block = core.create_enemy_block()
    enemies = enemy_block.UNITS
    X_UPPER_BOUNDARY_PLAYER = (
        configurations.SCREEN_BOUNDARY_X - player.IMG_WIDTH
    )
    X_UPPER_BOUNDARY_ENEMY = (
        configurations.SCREEN_BOUNDARY_X - Enemy.IMG_WIDTH
    )  # assuming all enemies use same image


if __name__ == "__main__":
    game_init()
    main()

#!/usr/bin/env python3
# Standard Library Imports
import random

# Third Party Imports
import pygame
from pygame import mixer

# Local Application Imports
import core
from classes.enemyblock import EnemyBlock
from classes.block import Block
from classes.gameobject import (
    Player,
    Score,
)
from configurations import (
    SCREEN_BOUNDARY_X,
    SCREEN_BOUNDARY_Y,
    DISPLAY_CAPTION,
    ICON_PATH,
    BACKGROUND_MUSIC_PATH,
    NOT_INITIALIZED,
    NUMBER_OF_BLOCKS,
    BLACK,
    POINTS_PER_KILL,
)

pygame.init()

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
score = NOT_INITIALIZED
player = NOT_INITIALIZED
logical_enemy_block = NOT_INITIALIZED
on_screen_enemy_block = NOT_INITIALIZED
bullets = NOT_INITIALIZED

# Blocks, or barriers
blocks = core.create_blocks(NUMBER_OF_BLOCKS)


def main():

    global logical_enemy_block
    global bullets
    # Game Loop
    VICTORY_MESSAGE = "YOU WON!"
    DEFEAT_MESSAGE = "DEFEATED!"
    game_over_message = None
    running = True
    game_over = False

    while running:

        # RGB
        screen.fill((0, 180, 0))
        running = core.check_events(player)

        for block in blocks:
            block.blit(screen, BLACK)

        if game_over:
            core.do_game_over(on_screen_enemy_block, screen, game_over_message)

        # player movement
        # player should be stopped on the x axis when the icon_width + position
        # are about to go out of the upper or lower x boundary
        if core.is_player_outof_bounds(player):
            player.x_cord_change = 0
        if core.is_bullet_init(player):
            if player.bullet not in bullets:
                bullets.append(player.bullet)
            if player.bullet.is_off_screen():
                bullets.remove(player.bullet)
                player.reset_bullet()

        # enemy movement
        # enemy should be stopped on the x axis when the icon_width + position
        # are about to go out of the upper or lower x boundary
        for enemy in on_screen_enemy_block:
            player_enemy_collision = core.is_collision(
                player.x_cord, enemy.x_cord, player.y_cord, enemy.y_cord
            )
            if player_enemy_collision:
                game_over = True
                game_over_message = DEFEAT_MESSAGE
                break
            bullet_enemy_collision = (
                core.is_collision(
                    enemy.x_cord,
                    player.bullet.x_cord,
                    enemy.y_cord,
                    player.bullet.y_cord,
                )
                if core.is_bullet_init(player)
                else False
            )
            if bullet_enemy_collision:
                core.destroy_enemy(
                    enemy, on_screen_enemy_block, logical_enemy_block,
                )
                player.reset_bullet()
                score.add_points(POINTS_PER_KILL)
                continue
            elif core.is_enemy_out_of_lower_bounds(enemy):
                core.go_down_right(on_screen_enemy_block, screen)
                break
            elif core.is_enemy_out_of_upper_bounds(enemy):
                core.go_down_left(on_screen_enemy_block, screen)
                break
            enemy.blit(screen)
            enemy.x_cord += enemy.x_cord_change

        # Choosing enemy to fire bullet (and if to)
        enemy_choice = random.randint(0, Block.NODES_PER_ROW)
        enemy = EnemyBlock.DESTROYED_ENEMY_SLOT
        row_index = -1
        while enemy is EnemyBlock.DESTROYED_ENEMY_SLOT:
            if abs(row_index) >= Block.NODES_PER_COLUMN:
                break
            enemy = logical_enemy_block.STRUCTURE[row_index][enemy_choice]
            row_index -= 1
            # If the enemy selected on the last row does not exist
            # (or EnemyBlock.DESTROYED_ENEMY_SLOT)
            # Look at the same enemy index on the row above

        if core.should_enemy_fire(enemy):
            bullets.append(enemy.bullet_init())

        # Bullet movement
        for bullet in bullets:
            if(game_over):
                break
            continue_tracking_bullet = core.track_bullet_movement(
                bullet, blocks, screen
            )
            if not continue_tracking_bullet:
                bullets.remove(bullet)
                bullet.reset_bullet()
                continue
            if bullet is not player.bullet:
                bullet_player_collision = core.is_collision(
                    bullet.x_cord, player.x_cord, bullet.y_cord, player.y_cord,
                )
                if bullet_player_collision:
                    bullets.remove(bullet)
                    game_over = True
                    game_over_message = DEFEAT_MESSAGE
                    break

        if len(on_screen_enemy_block) == 0:
            game_over = True
            game_over_message = VICTORY_MESSAGE

        player.blit(screen)
        player.x_cord += player.x_cord_change
        core.show_score(score, screen)
        pygame.display.update()


def game_init():

    global player
    global on_screen_enemy_block
    global logical_enemy_block
    global bullets
    global score
    player = Player()
    score = Score()
    bullets = list()
    logical_enemy_block = core.create_enemy_block()
    on_screen_enemy_block = logical_enemy_block.UNITS


if __name__ == "__main__":
    game_init()
    main()

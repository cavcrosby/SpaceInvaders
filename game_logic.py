# Standard Library Imports

# Third Party Imports
import pygame
from pygame import mixer

# Local Application Imports
import util
from classes.bullet import Bullet
from classes.enemy import Enemy
from main import (
    BULLET_SHOOTING_SOUND_PATH,
    SCREEN_OUT_OF_BOUNDS_Y,
    EXPLOSION_SOUND_PATH,
    POINTS_PER_KILL,
    SCREEN_BOUNDARY_X,
)

OFF_SCREEN = -1


def draw_blocks(screen, blocks):

    for block in blocks:
        util.draw_block(screen, block)


def do_game_over(enemies, screen):

    for enemy in enemies:
        enemy.y_cord = SCREEN_OUT_OF_BOUNDS_Y
    util.game_over_text(screen)


def go_down_right(enemy):

    enemy.x_cord_change = 0.75
    enemy.y_cord += enemy.y_cord_change


def go_down_left(enemy):

    enemy.x_cord_change = -0.75
    enemy.y_cord += enemy.y_cord_change


def check_events(player, bullet):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_cord_change = -0.6
            if event.key == pygame.K_RIGHT:
                player.x_cord_change = 0.6
            if (
                event.key == pygame.K_SPACE
                and Bullet.bullet_state is Bullet.BULLET_READY
            ):
                Bullet.bullet_state = Bullet.BULLET_FIRE
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_cord_change = 0

    return True


def check_block_bullet_collisions(bullet, blocks):

    for block in blocks:
        for rec in block.STRUCTURE:
            bullet_rec_collision = util.is_collision(
                rec.x, bullet.x_cord, rec.y, bullet.y_cord
            )
            if bullet_rec_collision:
                block.STRUCTURE.remove(rec)
                bullet.y_cord = OFF_SCREEN
                Bullet.bullet_state = Bullet.BULLET_READY
                break


def bullet_init(player):

    bullet = Bullet(player)
    bullet_sound = mixer.Sound(BULLET_SHOOTING_SOUND_PATH)
    bullet_sound.play()
    Bullet.ON_SCREEN = True
    return bullet


def reset_bullet():

    Bullet.bullet_state = Bullet.BULLET_READY
    Bullet.ON_SCREEN = False


def check_enemy_bullet_collisions(bullet, enemy):

    return (
        util.is_collision(enemy.x_cord, bullet.x_cord, enemy.y_cord, bullet.y_cord)
        if Bullet.bullet_state is Bullet.BULLET_FIRE
        else False
    )


def destroy_enemy(bullet, enemy, enemies, score):

    explosion_sound = mixer.Sound(EXPLOSION_SOUND_PATH)
    explosion_sound.play()
    bullet.y_cord = OFF_SCREEN
    Bullet.bullet_state = Bullet.BULLET_READY
    score.add_points(POINTS_PER_KILL)
    enemies.remove(enemy)
    enemies.append(Enemy(SCREEN_BOUNDARY_X))

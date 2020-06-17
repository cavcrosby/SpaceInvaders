#!/usr/bin/env python3
# Standard Library Imports

# Third Party Imports
import pygame
from pygame import mixer

# Local Application Imports
import util
from classes.player import Player
from classes.enemy import Enemy
from classes.bullet import Bullet
from classes.score import Score
from classes.block.block import Block

pygame.init()

# configurations

SCREEN_BOUNDARY_X = 800
SCREEN_BOUNDARY_Y = 600
NUMBER_OF_ENEMIES = 12
POINTS_PER_KILL = 20

# non-user configurations

SCREEN_OUT_OF_BOUNDS_Y = SCREEN_BOUNDARY_Y * 5
DISPLAY_CAPTION = "Space Invaders"
ICON_PATH = "./images/ufo.png"
BACKGROUND_MUSIC_PATH = "./music/background.wav"
BULLET_SHOOTING_SOUND_PATH = "./music/laser.wav"
EXPLOSION_SOUND_PATH = "./music/explosion.wav"

# creates the screen
screen = pygame.display.set_mode((SCREEN_BOUNDARY_X, SCREEN_BOUNDARY_Y))

# Caption and Icon
pygame.display.set_caption(DISPLAY_CAPTION)
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)

# Sound
mixer.music.load(BACKGROUND_MUSIC_PATH)
mixer.music.play(-1)

score = Score()
player = None
enemies = None
bullet = None

# block 1

b1 = Block((125, 350), (175, 400))
b2 = Block((275, 350), (325, 400))
b3 = Block((425, 350), (475, 400))
b4 = Block((575, 350), (625, 400))

blocks = [b1, b2, b3, b4]


def main():

    # Loop Configurations
    UPPER_BOUNDARY_PLAYER = SCREEN_BOUNDARY_X - player.IMG_WIDTH
    UPPER_BOUNDARY_ENEMY = (
        SCREEN_BOUNDARY_X - enemies[0].IMG_WIDTH
    )  # assuming all enemies use same image
    LOWER_BOUNDARY = 0

    # Game Loop
    running = True
    game_over = False
    while running:

        # RGB
        screen.fill((0, 180, 0))

        for block in blocks:
            util.draw_block(screen, block)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_cord_change = -0.6
                if event.key == pygame.K_RIGHT:
                    player.x_cord_change = 0.6
                if (
                    event.key == pygame.K_SPACE
                    and Bullet.bullet_state is Bullet.BULLET_READY
                ):
                    global bullet
                    bullet_sound = mixer.Sound(BULLET_SHOOTING_SOUND_PATH)
                    bullet_sound.play()
                    bullet = Bullet(player)
                    Bullet.bullet_state = Bullet.BULLET_FIRE
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.x_cord_change = 0

        # player movement
        # player should be stopped on the x axis when the icon_width + position are about to
        # go out of the upper or lower x boundary
        if (player.x_cord + player.x_cord_change < LOWER_BOUNDARY) or (
            player.x_cord + player.x_cord_change > UPPER_BOUNDARY_PLAYER
        ):
            player.x_cord_change = 0

        # enemy movement
        # enemy should be stopped on the x axis when the icon_width + position are about to
        # go out of the upper or lower x boundary
        for enemy in enemies:
            # Collision
            bullet_enemy_collision = (
                util.is_collision(
                    enemy.x_cord, bullet.x_cord, enemy.y_cord, bullet.y_cord
                )
                if Bullet.bullet_state is Bullet.BULLET_FIRE
                else False
            )
            player_enemy_collision = util.is_collision(
                enemy.x_cord, player.x_cord, enemy.y_cord, player.y_cord,
            )
            if player_enemy_collision or game_over:
                for enemy in enemies:
                    enemy.y_cord = SCREEN_OUT_OF_BOUNDS_Y
                util.game_over_text(screen)
                game_over = True
                break
            if bullet_enemy_collision:
                explosion_sound = mixer.Sound(EXPLOSION_SOUND_PATH)
                explosion_sound.play()
                bullet.y_cord = player.y_cord
                Bullet.bullet_state = Bullet.BULLET_READY
                score.add_points(POINTS_PER_KILL)
                enemies.remove(enemy)
                enemies.append(Enemy(SCREEN_BOUNDARY_X))
            elif enemy.x_cord + enemy.x_cord_change < LOWER_BOUNDARY:
                enemy.x_cord_change = 0.75
                enemy.y_cord += enemy.y_cord_change
            elif enemy.x_cord + enemy.x_cord_change > UPPER_BOUNDARY_ENEMY:
                enemy.x_cord_change = -0.75
                enemy.y_cord += enemy.y_cord_change
            enemy.x_cord += enemy.x_cord_change
            util.draw_baseobject(enemy, screen)

        # Bullet Movement
        if Bullet.bullet_state is Bullet.BULLET_FIRE:
            util.fire_bullet(bullet, screen)
            bullet.y_cord -= bullet.y_change
            if bullet.y_cord < 0:
                Bullet.bullet_state = Bullet.BULLET_READY
            for block in blocks:
                for rec in block.STRUCTURE:
                    bullet_rec_collision = util.is_collision(
                        rec.x, bullet.x_cord, rec.y, bullet.y_cord
                    )
                    if bullet_rec_collision:
                        block.STRUCTURE.remove(rec)
                        bullet.y_cord = -1
                        Bullet.bullet_state = Bullet.BULLET_READY
                        break

        player.x_cord += player.x_cord_change
        util.draw_baseobject(player, screen)
        util.show_score(score, screen)
        pygame.display.update()


def game_init():
    global player, enemies
    player = Player()
    enemies = [Enemy(SCREEN_BOUNDARY_X) for i in range(NUMBER_OF_ENEMIES)]


if __name__ == "__main__":
    game_init()
    main()

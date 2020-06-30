# Standard Library Imports
import math

# Third Party Imports
import pygame
from pygame import mixer

# Local Application Imports
import configurations
from classes.rectblock import RectBlock
from classes.enemyblock import EnemyBlock
from classes.gameobject import Bullet


def show_score(score, screen):

    font = pygame.font.Font(configurations.GAME_FONT, 25)
    score_text = font.render(
        "Score: " + str(score.value), True, (255, 255, 255)
    )
    screen.blit(score_text, (score.x_cord, score.y_cord))


def bullet_init(player):

    bullet = Bullet(player)
    bullet_sound = mixer.Sound(configurations.BULLET_SHOOTING_SOUND_PATH)
    bullet_sound.play()
    Bullet.ON_SCREEN = True
    return bullet


def do_game_over(enemies, screen):
    
    def show_game_over_text():

        font = pygame.font.Font(configurations.GAME_FONT, 64)
        text = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(text, (200, 250))

    for enemy in enemies:
        enemy.y_cord = configurations.OFF_SCREEN
    show_game_over_text()


def go_down_right(enemies, screen):

    for enemy in enemies:
        enemy.x_cord_change = configurations.DEFAULT_ENEMY_SPEED
        enemy.y_cord += enemy.y_cord_change
        enemy.blit(screen)
        enemy.x_cord += enemy.x_cord_change


def go_down_left(enemies, screen):

    for enemy in enemies:
        enemy.x_cord_change = configurations.DEFAULT_ENEMY_SPEED * -1
        enemy.y_cord += enemy.y_cord_change
        enemy.blit(screen)
        enemy.x_cord += enemy.x_cord_change


def is_collision(x1, x2, y1, y2):

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance < 27:
        return True
    return False


def destroy_enemy(bullet, enemy, enemies, score):

    explosion_sound = mixer.Sound(configurations.EXPLOSION_SOUND_PATH)
    explosion_sound.play()
    bullet.y_cord = configurations.OFF_SCREEN
    Bullet.reset_bullet_state()
    score.add_points(configurations.POINTS_PER_KILL)
    enemies.remove(enemy)


def react_block_bullet_collision(block, bullet, rect):

    block.remove_unit(rect)
    bullet.y_cord = configurations.OFF_SCREEN
    Bullet.bullet_state = Bullet.BULLET_READY


def is_block_bullet_collision(blocks, bullet):

    for block in blocks:
        for rect in block.UNITS:
            bullet_block_collision = is_collision(
                bullet.x_cord, rect.x, bullet.y_cord, rect.y
            )
            if bullet_block_collision:
                return {"block": block, "rect": rect}

    return None


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


def create_blocks(number_of_blocks):

    blocks = []
    STARTING_X_RANGE = 0
    ENDING_X_RANGE = 800
    BLOCK_WIDTH = 90
    DISTANCE_BETWEEN_TOP_LEFT_BLOCKS = 150
    DISTANCE_BETWEEN_BLOCKS = DISTANCE_BETWEEN_TOP_LEFT_BLOCKS - BLOCK_WIDTH
    # [DISTANCE_BETWEEN_BLOCKS] is just the 'empty' space between blocks.

    BLOCK_HEIGHT_TOP = 375
    BLOCK_HEIGHT_BOTTOM = 460
    TOTAL_WIDTH = (BLOCK_WIDTH * number_of_blocks) + (
        DISTANCE_BETWEEN_BLOCKS * (number_of_blocks - 1)
    )
    # [TOTAL_WIDTH] This is total amount of width taken up by all the blocks
    # plus their distances between them (number_of_blocks - 1).

    BLOCKS_X_RANGE = ENDING_X_RANGE - STARTING_X_RANGE
    # [BLOCKS_X_RANGE] This is the range that the blocks and
    # their distances can take up.

    TOP_LEFT_START = (BLOCKS_X_RANGE - TOTAL_WIDTH) / 2

    for i in range(number_of_blocks):

        block = RectBlock(
            top_left=(TOP_LEFT_START, BLOCK_HEIGHT_TOP),
            bottom_right=(TOP_LEFT_START + BLOCK_WIDTH, BLOCK_HEIGHT_BOTTOM),
        )
        TOP_LEFT_START += DISTANCE_BETWEEN_TOP_LEFT_BLOCKS
        blocks.append(block)

    return blocks


def create_enemy_block():

    TOP_LEFT = (50, 50)
    BOTTOM_RIGHT = (100, 100)

    return EnemyBlock(TOP_LEFT, BOTTOM_RIGHT)

# Standard Library Imports
import math
import random

# Third Party Imports
import pygame
from pygame import mixer

# Local Application Imports
from classes.rectblock import RectBlock
from classes.enemyblock import EnemyBlock
from classes.gameobject import (
    Player,
    Enemy,
)
from configurations import (
    X_LOWER_BOUNDARY,
    GAME_FONT,
    NOT_INITIALIZED,
    OFF_SCREEN_Y_CORD,
    DEFAULT_ENEMY_SPEED,
    EXPLOSION_SOUND_PATH,
    DEFAULT_PLAYER_SPEED,
)


def show_score(score, screen):

    font = pygame.font.Font(GAME_FONT, 25)
    score_text = font.render(
        "Score: " + str(score.value), True, (255, 255, 255)
    )
    screen.blit(score_text, (score.x_cord, score.y_cord))


def is_player_outof_bounds(player):

    return player.x_cord + player.x_cord_change < X_LOWER_BOUNDARY or (
        player.x_cord + player.x_cord_change > Player.X_UPPER_BOUNDARY
    )


def is_enemy_out_of_upper_bounds(enemy):

    return enemy.x_cord + enemy.x_cord_change > Enemy.X_UPPER_BOUNDARY


def is_enemy_out_of_lower_bounds(enemy):

    return enemy.x_cord + enemy.x_cord_change < X_LOWER_BOUNDARY


def should_enemy_fire(enemy):

    if enemy is not EnemyBlock.DESTROYED_ENEMY_SLOT:
        return random.randint(1, 250) == 1
    return False


def is_bullet_init(gameobject):

    return gameobject.bullet is not NOT_INITIALIZED


def track_bullet_movement(bullet, blocks, screen):

    if bullet.is_off_screen():
        bullet.reset_bullet()
        return False
    else:
        bullet.blit(screen)
        bullet.y_cord -= bullet.y_change
        bullet_block_collision = False
        bullet_block_collision = is_block_bullet_collision(blocks, bullet)
        if bullet_block_collision is not None:
            bullet_block_collision["block"].remove_node_from_row(
                bullet_block_collision["rect"]
            )
            return False
        return True


def do_game_over(enemies, screen, sub_text_message):
    def show_game_over_text():

        font = pygame.font.Font(GAME_FONT, 64)
        text = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(text, (200, 250))

        font = pygame.font.Font(GAME_FONT, 32)
        sub_text = font.render(sub_text_message.upper(), True, (255, 255, 255))
        screen.blit(sub_text, (205, 315))

    for enemy in enemies:
        enemy.y_cord = OFF_SCREEN_Y_CORD
    show_game_over_text()


def go_down_right(enemies, screen):

    for enemy in enemies:
        enemy.x_cord_change = DEFAULT_ENEMY_SPEED
        enemy.y_cord += enemy.y_cord_change
        enemy.blit(screen)
        enemy.x_cord += enemy.x_cord_change


def go_down_left(enemies, screen):

    for enemy in enemies:
        enemy.x_cord_change = DEFAULT_ENEMY_SPEED * -1
        enemy.y_cord += enemy.y_cord_change
        enemy.blit(screen)
        enemy.x_cord += enemy.x_cord_change


def is_collision(x1, x2, y1, y2):

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance < 27:
        return True
    return False


def destroy_enemy(enemy, on_screen_enemy_block, logical_enemy_block):

    explosion_sound = mixer.Sound(EXPLOSION_SOUND_PATH)
    explosion_sound.play()
    on_screen_enemy_block.remove(enemy)
    logical_enemy_block.replace_enemy(enemy, EnemyBlock.DESTROYED_ENEMY_SLOT)


def is_block_bullet_collision(blocks, bullet):

    for block in blocks:
        for rect in block.UNITS:
            bullet_block_collision = is_collision(
                bullet.x_cord, rect.x, bullet.y_cord, rect.y
            )
            if bullet_block_collision:
                return {"block": block, "rect": rect}

    return None


def check_events(player):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_cord_change = -1 * DEFAULT_PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                player.x_cord_change = DEFAULT_PLAYER_SPEED
            if (
                event.key == pygame.K_SPACE
                and player.bullet is NOT_INITIALIZED
            ):
                player.bullet_init()
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

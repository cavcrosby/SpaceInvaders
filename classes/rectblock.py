# Standard Library Imports

# Third Party Imports
import pygame
from pygame import Rect

# Local Application Imports
from classes.block import Block


class RectBlock(Block):
    def __init__(
        self,
        top_left,
        bottom_right,
        NODES_PER_COLUMN=Block.DEFAULT_PARENT_VALUE,
        NODES_PER_ROW=Block.DEFAULT_PARENT_VALUE,
    ):

        super().__init__(top_left, bottom_right)
        if NODES_PER_COLUMN is not self.DEFAULT_PARENT_VALUE:
            self.NODES_PER_COLUMN = NODES_PER_COLUMN
        if NODES_PER_ROW is not self.DEFAULT_PARENT_VALUE:
            self.NODES_PER_ROW = NODES_PER_ROW
        self._create_block()

    def _determine_total_width(self):

        return abs(self.bottom_right[self.X_CORD] - self.top_left[self.X_CORD])

    def _determine_total_height(self):

        return abs(self.bottom_right[self.Y_CORD] - self.top_left[self.Y_CORD])

    def _determine_node_height(self, total_height):

        return total_height / self.NODES_PER_COLUMN

    def _determine_node_width(self, total_width):

        return total_width / self.NODES_PER_ROW

    def _return_node(self, left, top, node_width, node_height):

        return Rect(left, top, node_width, node_height,)

    def blit(self, screen, COLOR):

        for rect in self.UNITS:
            pygame.draw.rect(screen, COLOR, rect)

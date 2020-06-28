# Standard Library Imports

# Third Party Imports

# Local Application Imports
from classes.block import Block
from classes.enemy import Enemy


class EnemyBlock(Block):
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

        total_width = abs(
            self.bottom_right[self.X_CORD] - self.top_left[self.X_CORD]
        )
        width_needed = Enemy.IMG_WIDTH * self.NODES_PER_ROW
        if total_width < width_needed:
            total_width += abs(total_width - width_needed)
        elif total_width > width_needed:
            total_width -= abs(total_width - width_needed)

        return total_width

    def _determine_total_height(self):

        total_height = abs(
            self.bottom_right[self.Y_CORD] - self.top_left[self.Y_CORD]
        )
        height_needed = (
            Enemy.IMG_WIDTH * self.NODES_PER_COLUMN
        )  # assuming icons have same width and height
        if total_height < height_needed:
            total_height += abs(total_height - height_needed)
        elif total_height > height_needed:
            total_height -= abs(total_height - height_needed)

        return total_height

    def _determine_node_height(self, total_height):

        return Enemy.IMG_WIDTH

    def _determine_node_width(self, total_width):

        return Enemy.IMG_WIDTH

    def _return_node(self, left, top, node_width, node_height):

        return Enemy.from_manual_cords(top, left)

    def blit(self, screen, COLOR):

        pass

# Standard Library Imports
from abc import (
    ABC,
    abstractmethod,
)

# Third Party Imports

# Local Application Imports


class Block(ABC):

    DEFAULT_PARENT_VALUE = "default"
    NODES_PER_COLUMN = 5
    NODES_PER_ROW = 4
    X_CORD = 0
    Y_CORD = 1

    @property
    def UNITS(self):

        return [node for row in self._structure for node in row]

    @property
    def STRUCTURE(self):

        return self._structure

    def __init__(self, top_left, bottom_right):

        self._structure = list()
        self.top_left = top_left
        self.bottom_right = bottom_right

    def remove_node_from_row(self, node):

        for row in self._structure:
            if node in row:
                row.remove(node)

    def _create_block(self):

        left = self.top_left[self.X_CORD]
        top = self.top_left[self.Y_CORD]
        total_width = self._determine_total_width()
        total_height = self._determine_total_height()
        NODE_HEIGHT = self._determine_node_height(total_height)
        NODE_WIDTH = self._determine_node_width(total_width)

        for row_n in range(self.NODES_PER_ROW):
            top_copy = top
            col = list()
            for col_n in range(self.NODES_PER_COLUMN):
                col.append(
                    self._return_node(left, top_copy, NODE_WIDTH, NODE_HEIGHT)
                )
                top_copy += NODE_HEIGHT - 1
            self._structure.append(col)
            left += NODE_WIDTH - 1
            # ({NODE_WIDTH,NODE_HEIGHT} - 1)
            # this is to make nodes appear as one block
            # layering of the nodes is done top-down, right (repeat)

    @abstractmethod
    def _determine_total_width(self):

        NotImplemented

    @abstractmethod
    def _determine_total_height(self):

        NotImplemented

    @abstractmethod
    def _determine_node_height(self, total_height):

        NotImplemented

    @abstractmethod
    def _determine_node_width(self, total_width):

        NotImplemented

    @abstractmethod
    def _return_node(self, left, top, node_width, node_height):

        NotImplemented

    @abstractmethod
    def blit(self):

        NotImplemented

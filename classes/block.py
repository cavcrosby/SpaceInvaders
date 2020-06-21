# Standard Library Imports

# Third Party Imports
from pygame.rect import Rect

# Local Application Imports


class Block:

    RECTS_PER_COLUMN = 5
    RECTS_PER_ROW = 4

    @property
    def STRUCTURE(self):

        return self._structure

    def __init__(self, top_left, bottom_right):

        self._structure = list()
        X_CORD = 0
        Y_CORD = 1

        left = top_left[X_CORD]
        top = top_left[Y_CORD]
        total_width = abs(bottom_right[X_CORD] - top_left[X_CORD])
        total_height = abs(bottom_right[Y_CORD] - top_left[Y_CORD])
        HEIGHT_REC_SIZE = total_height / self.RECTS_PER_COLUMN
        WIDTH_REC_SIZE = total_width / self.RECTS_PER_ROW

        for row_n in range(self.RECTS_PER_ROW):
            top_copy = top
            for col_n in range(self.RECTS_PER_COLUMN):
                self._structure.append(
                    Rect(left, top_copy, WIDTH_REC_SIZE, HEIGHT_REC_SIZE,)
                )
                top_copy += HEIGHT_REC_SIZE - 1
            left += WIDTH_REC_SIZE - 1
            # ({WIDTH_REC_SIZE,HEIGHT_REC_SIZE} - 1)
            # this is to make Rects appear as one block
            # layering of the Rects is done top-down, right (repeat)


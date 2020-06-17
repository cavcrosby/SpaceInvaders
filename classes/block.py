# Standard Library Imports

# Third Party Imports
from pygame.rect import Rect

# Local Application Imports

class Block:

    RECTS_PER_COLUMN = 4
    RECTS_PER_ROW = 3

    @property
    def STRUCTURE(self):

        return self._structure

    def __init__(self, top_left, bottom_right):

        self._structure = list()
        X_CORD = 0
        Y_CORD = 1

        left = top_left[X_CORD]
        top = top_left[Y_CORD]
        width = abs(bottom_right[X_CORD] - top_left[X_CORD])
        height = abs(bottom_right[Y_CORD] - top_left[Y_CORD])
        TOP_DECREMENT = height/self.RECTS_PER_COLUMN
        LEFT_DECREMENT = width/self.RECTS_PER_ROW

        for row_n in range(self.RECTS_PER_ROW):
            top_copy = top
            for col_n in range(self.RECTS_PER_COLUMN):
                self._structure.append(
                    Rect(
                        left,
                        top_copy,
                        width,
                        height,
                    )
                )
                top_copy += TOP_DECREMENT
            left += LEFT_DECREMENT


b = Block((0,0), (1, 1))
#print(len(b.STRUCTURE))
print(b.STRUCTURE[0].y)
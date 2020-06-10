# Standard Library Imports

# Third Party Imports

# Local Application Imports
from classes.baseobject import BaseObject


class Score(BaseObject):

    IMG = None

    def __init__(self):

        super().__init__(x_cord=10, y_cord=10)
        self.value = 0

    def add_points(self, points):

        if points >= 0:
            self.value += points

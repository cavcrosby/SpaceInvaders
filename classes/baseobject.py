# Standard Library Imports
from abc import ABC, abstractproperty

# Third Party Imports

# Local Application Imports


class BaseObject(ABC):
    @abstractproperty
    def IMG(self):

        NotImplemented

    @property
    def NO_IMG(self):

        return None

    def __init_subclass__(cls, *args, **kwargs):
        """Specifications required by future SpaceInvader subclasses."""
        super().__init_subclass__(*args, **kwargs)

        if cls.IMG is NotImplemented:
            raise NotImplementedError(
                f"Error: IMG not implemented in {cls.__name__}"
            )

    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def blit(self, screen):
        if self.IMG == self.NO_IMG:
            raise ValueError(
                f"No image is set for the {type(self).__name__} object!"
            )
        screen.blit(self.IMG, (self.x_cord, self.y_cord))

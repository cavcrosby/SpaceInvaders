# Standard Library Imports

# Third Party Imports

# Local Application Imports


class BaseObject:

    IMG = NotImplemented

    def __init_subclass__(cls, *args, **kwargs):
        """Specifications required by future SpaceInvader subclasses."""
        super().__init_subclass__(*args, **kwargs)

        if cls.IMG is NotImplemented:
            raise NotImplementedError(f"Error: IMG not implemented in {cls.__name__}")

    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord

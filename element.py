from error import UnimplementedError


class Element:
    '''
    This is the base class of all drawables in the project.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        raise UnimplementedError()


class canvas:
    def __init__(self, width, height):
        self.canvas = [[]*width for i in range(height)]

    def set(self, x, y, value):
        self.canvas[x][y] = value

    def get(self, x, y):
        return self.canvas[x][y]

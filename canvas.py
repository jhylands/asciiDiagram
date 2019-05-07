class Canvas:
    def __init__(self, width, height):
        self.canvas = [' '*width for i in range(height)]
        self.objs = []

    def set(self, x, y, value):
        self.canvas[x][y] = value

    def get(self, x, y):
        return self.canvas[x][y]

    def __str__(self):
        return '\n'.join(self.canvas)

    def draw(self, obj):
        try:
            ps = obj.__vector__()
            for x, y, val in ps:
                self.canvas[x][y] = val
        except AttributeError:
            print('Object not drawable')

    def draw_all(self):
        for obj in self.objs:
            self.draw(obj)

from canvas import Canvas
from element import Element

def line(x1, y1, x2, y2):
    buf = ""
    for x in range(x1, x2):
        Canvas.set(x,y1, '-')
    for y in range(y1, y2):
        Canvas.set(x1, y , '|')
    # how do we know which side the + is on 
    # if x1<x2 +----
    # else ---+
    "-"*(x2-x1)
    "+"
    "|"


class Line(Element):
    def __init__(self, x, y, dest_x, dest_y):
        super(Line).__init__(x, y)
        self.dest_x = dest_x
        self.dest_y = dest_y

    def draw(self, canvas):
        '''
        draw function takes a canvas object and writes the line to it.
        The function modifies the canvas object but doesn't return anything
        '''


def line(x1,y1,x2,y2):
    buf = ""
    for x in range(x1,x2):
        canvas.set(x,y1,'-')
    for y in range(y1,y2):
        canvas.set(x1, y , '|')
    # how do we know which side the + is on 
    # if x1<x2 +----
    # else ---+
    "-"*(x2-x1)
    "+"
    "|"
    

class canvas:
    def __init__(self, width, height):
        self.canvas = [[]*width for i in range(height)]

    def set(self, x, y, value):
        self.canvas[x][y] = value

    def get(self, x, y):
        return self.canvas[x][y]

        

ref line(x1,y1,x2,y2):
    buf = ""
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

        

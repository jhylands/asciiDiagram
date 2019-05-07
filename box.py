import Element

def box(width, height):
    buffer = []
    buffer.append("." + "-"*(width-2) + ".")
    buffer.extend(["|" + " "*(width-2) + "|" for i in range(height-2)])
    buffer.append("'" + "-"*(width-2) + "'")
    return "\n".join(buffer)


class Box(Element):

    def __init__(self, x, y, width, height):
        super(Box).__init__(x, y)
        self.width = width
        self.height = height

    def get_obj(self):
        # 
        pass

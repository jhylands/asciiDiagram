from error import UnimplementedError
from box import Box


def textbox(text):
    top = "." + "-"*(len(text)) + "."
    middle = "|" + text + "|"
    bottom = "'" + "-"*len(text)
    return "\n".join([top, middle, bottom])


class Textbox(Box):
    def __init__(self, text, x, y):
        width = len(text) + 2
        height = 3
        super(Textbox).__init__(x, y, width, height)

    def set_text(self, text):
        self.text = text

    def set_padding(self, padding):
        raise UnimplementedError()

def textbox(text):
    top = "." + "-"*(len(text)) +"."
    middle = "|" + text + "|"
    bottom = "'" + "-"*len(text)
    return "\n".join([top, middle, bottom])

import Element
class textbox(Element):
    def __init__(self):
        pass

    def set_text(self, text):
        self.text = text

    def set_padding(self, padding):
        raise UnimplementedError()

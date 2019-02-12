def textbox(text):
    top = "." + "-"*(len(text)) +"."
    middle = "|" + text + "|"
    bottom = "'" + "-"*len(text)
    return "\n".join([top, middle, bottom])

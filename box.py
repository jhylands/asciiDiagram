def box(width, height):
    buffer = []
    buffer.append("." + "-"*(width-2) + ".")
    buffer.extend(["|" + " "*(width-2) + "|" for i in range(height-2)])
    buffer.append("'" + "-"*(width-2) + "'")
    return "\n".join(buffer)

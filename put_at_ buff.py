def put_at_buff(buffer, x, y, thing):
    lines_of_buffer = buffer.split('\n')
    lines_of_thing = thing.split('\n')
    width = max(x + max([len(t) for t in lines_of_thing]), max([len(t) for t in lines_of_buffer]))
    height = max(y + len(lines_of_thing),len(lines_of_buffer))
    buffer = []
    for i in range(height):
        if i<len(lines_of_buffer):
            buffer.append(lines_of_buffer[i] + " "*(len(lines_of_buffer[i])-width))
        else:
            buffer.append(" "*width)
    #buffer = [" "*width +"|" for _ in range(height)]
    for i,line in enumerate(lines_of_thing):
        buffer[y+i] = buffer[y+i][:x] + line + buffer[y+i][x+len(line):]
    return "\n".join(buffer)

def put_at(x, y, thing):
    #find how big the containing box must be
    lines_of_thing = thing.split('\n')
    width = x + max([len(t) for t in lines_of_thing])
    height = y + len(lines_of_thing)
    buffer = [" "*width for x in range(height)]
    for i,line in enumerate(lines_of_thing):
        buffer[y+i] = buffer[y+i][:x] + line + buffer[y+i][x+len(line):]
    return "\n".join(buffer)

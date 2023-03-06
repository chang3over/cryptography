def center(s, width):
    if len(s) >= width:
        return s
    return " " * ((width - len(s)) // 2) + s

def get_color(index):
    if index < 33:
        color = 'red'
    elif index < 66:
        color = 'yellow'
    else:
        color = 'green'
    return color
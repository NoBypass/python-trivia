def colored(text, hexcode):
    if hexcode == 'blue': hexcode = '#3d8ef2'
    elif hexcode == 'red': hexcode = '#e62229'
    elif hexcode == 'yellow': hexcode = '#f5c311'
    elif hexcode == 'green': hexcode = '#3fb315'
    elif hexcode == 'u': hexcode = '#000000'
    else: hexcode = hexcode

    # inspired by https://www.reddit.com/r/learnpython/comments/bes286/how_do_i_print_colors_in_colorama_using_a_hex/
    # print in a hex defined color
    valid_hex = '0123456789ABCDEF'.__contains__
    hexint = int(''.join(filter(valid_hex, hexcode.upper())), 16)
    x = "\x1B[38;2;{};{};{}m{}\x1B[0m".format(hexint >> 16, hexint >> 8 & 0xFF, hexint & 0xFF, text)
    return x
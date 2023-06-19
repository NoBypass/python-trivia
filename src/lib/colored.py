def colored(text, hex_code):

    # check for aliases
    if hex_code == 'blue': hex_code = '#3d8ef2'
    elif hex_code == 'red': hex_code = '#e62229'
    elif hex_code == 'yellow': hex_code = '#f5c311'
    elif hex_code == 'green': hex_code = '#3fb315'
    elif hex_code == 'u': hex_code = '#000000'
    else: hex_code = hex_code

    # inspired by https://www.reddit.com/r/learnpython/comments/bes286/how_do_i_print_colors_in_colorama_using_a_hex/
    # print in a hex defined color
    valid_hex = '0123456789ABCDEF'.__contains__
    hexint = int(''.join(filter(valid_hex, hex_code.upper())), 16)
    x = "\x1B[38;2;{};{};{}m{}\x1B[0m".format(hexint >> 16, hexint >> 8 & 0xFF, hexint & 0xFF, text)
    return x
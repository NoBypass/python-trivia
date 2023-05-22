from menuLn import *


def menu(width, my_list):
    for i in range(len(my_list)):
        if isinstance(my_list[i], list):
            arg = my_list[i][0]
            color = my_list[i][1]
        else:
            arg = my_list[i]
            color = 'blue'
        menu_ln(width, arg, color, i, len(my_list))

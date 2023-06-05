from colored import *


def menu_ln(width, args, color, pos, max):
    if len(args) > width - 6: return print(args)  # print('Error: at function "menu"')
    if args == 'empty': return
    if args == 'full':
        if pos == 0:
            corners = ['╔', '╗']
        elif pos == max - 1:
            corners = ['╚', '╝']
        else:
            corners = ['╠', '╣']
        print(colored(corners[0] + '═' * (width - 2) + corners[1], 'blue'))
    else:
        x = int((width - len(args) - 2) / 2)
        if len(args) % 2 != 0:
            y = x + 1
        else:
            y = x
        main = colored(' ' * x + args + ' ' * y, color)
        print(colored('║', 'blue') + main + colored('║', 'blue'))


def menu(width, my_list):
    for i in range(len(my_list)):
        if isinstance(my_list[i], list):
            arg = my_list[i][0]
            color = my_list[i][1]
        else:
            arg = my_list[i]
            color = 'blue'
        menu_ln(width, arg, color, i, len(my_list))

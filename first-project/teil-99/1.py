import math
import random

def line(desc):
    if desc == 'full':
        return print('*' * 44)
    else:
        return print('** ' + desc + ' ' * (38 - len(desc)) + ' **')

line('full')
line('                Menu')
line('full')
line('       Commands / Description')
line('full')
line('    (1) Get surface of square')
line('    (2) Open save')
line('    (3) Mix the sentence')
line('    (4) Mix a word')
line('    (x) Input Exit')
line('full')

typeList = [
    '1',
    '2',
    '3',
    '4',
    'x',
]

def square(x):
    return x**2

def openSave(x):
    while x != '123':
        x = input('Secret code incorrect, please try again.\n>>> ')
    return print('Save opened!')

def diff(x, y):
    return print(x + ' - ' + y + ' = ' + str(int(x) - int(y)))

def rom(x):
    x = int(x)
    divList = [
        100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1
    ]
    symList = [
        'ↈ', 'ↇ', 'ↂ', 'ↁ', 'M', 'C', 'D', 'L', 'X', 'V', 'I'
    ]
    final = ''

    i = 0
    while x > 0:
        for _ in range(x // divList[i]):
            final += symList[i] + ' '
            x -= divList[i]
        i += 1
    return str(print(final))

rom(12345)
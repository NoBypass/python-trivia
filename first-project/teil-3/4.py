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
line('    (1) Get character count')
line('    (2) Get word count')
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
def mixList(s):
    randList = s.split(' ')
    random.shuffle(randList)
    final = ''
    for i in randList:
        final += i + ' '
    return final

def mixAll(s):
    randList = [*s]
    random.shuffle(randList)
    final = ''
    for i in randList:
        final += i
    return final


sentence = input('Please give me a sentence.\n>>> ')

while type != 'x':
    type = input('What command do you want to use?\n>>> ')
    while type not in typeList:
        type = int(input('Sorry, this command does not exist, please enter a valid one.\n>>> '))
    if type == '1':
        print('Character count: ' + str(len(sentence)))
    elif type == '2':
        print('Word count:' + str(len(sentence.split(' '))))
    elif type == '3':
        print('Mixed sentence: ' + str(mixList(sentence)))
    elif type == '4':
        print('VERY mixed sentence: ' + str(mixAll(sentence)))
    else:
        print('Exiting...')
        break
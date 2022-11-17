import random
sentence = input('Give me any sentence.\n>>> ')

def countWords(s):
    return print('Your sentence has ' + str(len(s.split(' '))) + ' words!')

def mixList(s):
    randList = s.split(' ')
    random.shuffle(randList)
    final = ''
    for i in randList:
        final += i + ' '
    return print(final)

mixList(sentence)
countWords(sentence)
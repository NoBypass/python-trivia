from colored import *


def validate(question, answerList):
    answer = input(colored('\n' + question + ' ▶ ', 'blue'))
    while answer not in answerList:
        answer = input(colored('Invalid ' + question + ', please choose one that exists' + ' ▶ ', 'blue'))
    return answer


def test(num): return num

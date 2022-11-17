from functions.colored import *

def trueFalse(question, correctAnswer):
    answer = input('\n' + question + ' \nPlease Answer with "True" or "False" (aliases are: 1 & 2, t & f) ▶ ')
    answerList = [
        'True',
        'False',
        '1',
        '2',
        't',
        'f',
        'quit',
        'skip'
    ]

    if correctAnswer == 'True':
        correctAnswers = ['True', '1', 't']
    else:
        correctAnswers = ['False', '2', 'f']

    while answer not in answerList:
        answer = input(colored('Please choose one of the following options:\n"True" or "False" (aliases are: 1 & 2, t & f) ▶ ', 'red'))
    if answer == 'skip':
        return [print(colored('You skipped this question. The answer would have been ' + correctAnswer, 'yellow')), 1, 0, False]
    if answer == 'quit':
        return [print(colored('You quit! What a shame! The answer would have been ' + correctAnswer, 'yellow')), 1, 0, True]
    if answer not in correctAnswers:
        return [print(colored('Wrong! The answer would have been ' + correctAnswer, 'red')), 1, 0, False]
    else:
        return [print(colored('Correct! ', 'green')), 0, 1, False]
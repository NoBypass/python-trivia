from lib.colored import *


def multiple_choice(question, correctAnswer, answers):
    mistakes = 0
    answer = input('\n' + question + ' Your options are: ' + answers + ' ▶ ')
    while answer != 'skip':
        if answer == 'quit':
            return [print(colored('You quit! What a shame! The answer would have been ' + correctAnswer, 'yellow')), 1,
                    0, True]
        if answer != 'a' and answer != 'b' and answer != 'c' and answer != 'd':
            answer = input(colored('Please choose one of the following options: \n' + answers + ' ▶ ', 'red'))
            continue
        elif answer != correctAnswer:
            mistakes += 1
            answer = input(colored('Your answer was incorrect, try again! ▶ ', 'red'))
            continue
        else:
            return [print(colored('Correct!', 'green')), mistakes, 1, False]
    mistakes += 1
    return [print(colored('You skipped this question. The answer would have been ' + correctAnswer, 'yellow')),
            mistakes, 0, False]

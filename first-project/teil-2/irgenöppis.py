from urllib.request import urlopen
from termcolor import colored
from random import seed
from random import randint
import json

fails = 0
correct = 0
i = 0
stop = False
done = []

cType = input('Do you want to play multiple choice (mc) or random (r)\n>>> ')

while cType != 'r' and cType != 'mc':
    cType = input('Please either type "mc" for multiple choice or "r" for random\n>>> ')

difficulty = input('What difficulty do you want to play? You can choose between easy, medium and hard\n>>> ')

while difficulty != 'easy' and difficulty != 'medium' and difficulty != 'hard':
    difficulty = input('Please either type "easy", "medium" or "hard".\n>>> ')

if cType == 'r':
    url = 'https://opentdb.com/api.php?amount=1&category=23&difficulty=' + difficulty
    print('Selected mode "random" on ' + difficulty + ' difficulty.')
elif cType == 'mc':
    url = 'https://opentdb.com/api.php?amount=1&category=23&difficulty=' + difficulty + '&type=multiple'
    print('Selected mode "multiple choice" on ' + difficulty + ' difficulty.')

while i < len('never'):
    response = urlopen(url)
    data = json.loads(response.read())

    question = data['results'][0]['question']
    question = question.replace('&quot;', '"')
    question = question.replace('&#039;', '\'')
    answer = data['results'][0]['correct_answer']
    type = data['results'][0]['type']

    options = '>>> '
    if type == 'multiple':
        pAnswers = [
            data['results'][0]['correct_answer'],
            data['results'][0]['incorrect_answers'][0],
            data['results'][0]['incorrect_answers'][1],
            data['results'][0]['incorrect_answers'][2],
        ]

        randint1 = randint(0, 4)
        randint2 = randint(0, 4)
        if randint2 == randint1:
            randint2 += 1
        if randint2 <= 5:
            randint2 = 1

        pAnswers[randint1 - 1], pAnswers[randint2 - 1] = pAnswers[randint2 - 1], pAnswers[randint1 - 1]
        desc = '(multiple choice)'
        options = 'a: ' + pAnswers[0] + ' b: ' + pAnswers[1] + ' c: ' + pAnswers[2] + ' d: ' + pAnswers[3] + ' >>> '
        aIndex = pAnswers.index(answer)
        if aIndex == 0:
            answer = 'a'
        elif aIndex == 1:
            answer = 'b'
        elif aIndex == 2:
            answer = 'c'
        elif aIndex == 3:
            answer = 'd'
        else:
            answer = answer
    elif answer == 'True' or answer == 'False':
        desc = '(true-false question) '
    else:
        desc = ''
    cAnswer = input(question + str(desc) + '\n' + str(options))
    if cAnswer == 'stop':
        break
    elif cAnswer == 'skip':
        print(colored('The correct answer would have been ' + answer, 'yellow'))
        fails += 1
        continue

    while cAnswer != answer:
        if cAnswer == 'skip':
            print(colored('The correct answer would have been ' + answer, 'yellow'))
            fails += 1
            break
        elif cAnswer == 'stop':
            print(colored('Please confirm that you want to quit by saying "stop" again.', 'red'))
            fails += 1
            break
        cAnswer = input(colored('Wrong answer! I repeat, ' + question + str(desc), 'red') + '\n' + str(options))
        fails += 1
    if cAnswer == answer:
        correct += 1
        print(colored('Correct! The answer was indeed ' + cAnswer + '!', 'green'))
print('You answered incorrectly ' + str(fails) + ' times.')
print('You answered correctly ' + str(correct) + ' times.')

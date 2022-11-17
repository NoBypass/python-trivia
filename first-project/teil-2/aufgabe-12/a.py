questionList = [
    'Where is rome?',
    'Does pineapple belong on Pizza?',
    'What was first; the chicken or the egg?'
]

answerList = [
    'Italy',
    'Yes',
    'Your mom',
]

i = 0
fails = 0
while i < len(questionList):
    answer = input(questionList[i] + ' ')
    while answer != answerList[i]:
        answer = input('Wrong answer! I repeat, ' + questionList[i])
        fails += 1
    print('Correct! The answer is indeed ' + answer + '!')
    i += 1
print('You answered incorrectly ' + str(fails) + ' times.')
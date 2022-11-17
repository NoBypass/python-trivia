answer = input('Give me any sentence: ')
answerList = answer.split(' ')
i = 0
for word in answerList:
    i += 1
    print(answerList[len(answerList) - i])
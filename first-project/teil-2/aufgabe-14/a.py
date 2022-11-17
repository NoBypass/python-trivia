sentenceList = input('Please give me a sentence: ').split(' ')

for i in range(len(sentenceList)):
    for j in range(len(sentenceList)):

        if sentenceList[i] < sentenceList[j]:
            sentenceList[i], sentenceList[j] = sentenceList[j], sentenceList[i]

print(sentenceList)


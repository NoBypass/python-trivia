file = open('./ReadMe.txt')
myText = file.read()
file.close()

newFile = open('./NewFile.txt', 'w')
newFile.write(myText.replace('*', ''))

arr = []
for i in myText:
    if myText.count(i) == 0:
        continue
    arr.append(str(myText.count(i)) + ' = ' + i)
    myText = myText.replace(i, '')
max = len(max(arr, key=len))
for i in sorted(arr):
    zero = '0' * (int(max) - len(i))
    print(zero + i)

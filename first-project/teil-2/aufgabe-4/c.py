num = int(input('Give me any number: '))
if num > 10000:
    num = int(input('This number was to high to process, sorry: '))
print(list(range(0, num+1)))
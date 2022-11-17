answer = input('What is 5+3: ')
fails = 0
while answer != '8':
    answer = input('Wrong answer! I repeat, what is 5+3: ')
    fails += 1
print('Correct! The answer is indeed', answer, '. You only got it wring about ', fails, ' times!')
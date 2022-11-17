word = input('Please input a word\n>>> ')
revWord = word[::-1]

if revWord.lower() == word.lower():
    print('Your word is a palindrom!')
else:
    print('Your word isn\'t a palindrom!')
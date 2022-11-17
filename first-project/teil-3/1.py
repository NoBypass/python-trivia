from termcolor import colored

yn = input('Start request: Yes(Y) or No(N)\n>>> ')
good = False


def is_float(e):
    try:
        float(e)
        return True
    except ValueError:
        return False


while yn != 'y' and yn != 'n' and yn != 'Y' and yn != 'N':
    yn = input('Invalid input, please answer with Y or N\n>>> ')

if yn == 'N' or yn == 'n':
    print('You chose no, exiting...')
else:
    year = input('Please enter a date (year)\n>>> ')
    while not is_float(year):
        year = input('Please enter a valid year\n>>> ')
    if int(year) % 4 != 0:
        if int(year) % 100 == 0:
            print(colored('Given year is not a leap year.', 'red'))
        print(colored('Given year is not a leap year.', 'red'))
    else:
        print(colored('Given year is a leap year.', 'green'))

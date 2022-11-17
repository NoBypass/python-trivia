name = input('Please enter your first name: ')
age = input(name + '? Cool name! Please enter your age as well: ')
age = int(age)

if age < 6:
    print(name + ', how are you even able to read!')
elif 15 < age < 18:
    print(name + ', you\'re barely unable to drink.')
elif age > 18:
    print(name + ', you could get a drivers licence!')
else:
    print(name + ', why would yo choose to be that age??')
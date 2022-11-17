name = input('Please enter your first name: ')
weight = input(name + '? Cool name! Please enter your weight as well (in kg): ')
size = input('Just one last thing. Please tell me your body size in "cm" and we\'re done: ')

size = int(size) / 100
bmi = int(weight) / size**3

print(name + ', your BMI is: ' + str(bmi))
text = None
try:
    file = open('eingabe.txt')
    my_text = file.read()
    file.close()
except:
    print("Error")

print("Der Text hat "+str(len(text.split(" ")))+" Worte.")
fName = input("Was ist dein Vorname?\n>>>")
if fName in text:
    print("Dein Vorname ist im text vorhanden")
else:
    print("Dein Vorname ist nicht im text vorhanden")
print("Wort nummer 17 lautet: "+str(text.split(" ")[16]))
print("Der Buchstabe \"a\" ist "+str(text .count("a"))+" mal im Text vorhanden.")
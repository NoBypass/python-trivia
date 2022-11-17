from functions.menuLn import *

def menu(width, myList):
    for i in range(len(myList)):
        if isinstance(myList[i], list):
            arg = myList[i][0]
            color = myList[i][1]
        else:
            arg = myList[i]
            color = 'blue'
        menuLn(width, arg, color, i, len(myList))
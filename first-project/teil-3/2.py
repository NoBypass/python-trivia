def isFloatingPointNumber(number):
    try:
        n = number.split(".")
        if len(n) == 2:
            return True
        else:
            return False
    except:
        return False
print(isFloatingPointNumber(str('ngiufd.bgiuzdsv')))

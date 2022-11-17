i = 0


def odd(num):
    if i % 2 != 0:
        return True
    else:
        return False


while i < 12:
    i += 1
    if not odd(i):
        continue
    print(i)
else:
    print('Loop done!')
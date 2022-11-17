list = []
for i in range(0, 101):
    list.append(i)

for i in list:
    if i % 2 == 0:
        list[i] = i + 1
    else:
        list[i] = i - 1
print(list)
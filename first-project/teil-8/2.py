def bubblesort(zahlen):
    i = len(zahlen)
    while i >=1 :
        for j in range(len(zahlen)-1):
            if zahlen[j] > zahlen[j+1]:
                zahlen[j+1], zahlen[j] = zahlen[j], zahlen[j+1]
        i = i - 1
    return zahlen

meineUnordnung = [2,99,45,14,8,5,23,1,25,9,4,6,345,54,69]
ich_YB_Ordnung = bubblesort(meineUnordnung)

print (ich_YB_Ordnung[::-1])
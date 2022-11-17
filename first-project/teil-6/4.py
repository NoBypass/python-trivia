def renameFile():
    fName = input('What is your first name?\n>>> ')
    lName = input('What is your last name?\n>>> ')
    try:
        txt = open('./test.txt', 'a')
        txt.write(fName + ' ' + lName)
        txt.close()
        print('Successfully wrote your name down.')
    except:
        print('Why\'d you get an error???')

renameFile()
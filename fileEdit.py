import os
from os import listdir
from os.path import isfile, join

def RemoveChar():
    os.system('cls')
    print("#Char Remove#")
    print("Please enter the character to remove from files:")
    charToRemove = input()

    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print("")
    print("###############")
    print("Files found:")
    for file in onlyfiles:
        print(file)
    print("###############")
    print("")
    print("Removing char: " + charToRemove)

    newNames = []
    for file in onlyfiles:
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = newName.replace(charToRemove, '')
        newName = newName + fileExtention
        newNames.append(newName)
        os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("ENTER to continue")
    input()

def ReplaceChar():
    os.system('cls')
    print("#Char Replace#")
    print("Please enter the char to remove:")
    charToRemove = input()
    print("Please enter the char to replace it with:")
    charToInsert = input()

    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print("")
    print("###############")
    print("Files found:")
    for file in onlyfiles:
        print(file)
    print("###############")
    print("")
    print("Replacing char: " + charToRemove + " with: " + charToInsert)

    newNames = []
    for file in onlyfiles:
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = newName.replace(charToRemove, charToInsert)
        newName = newName + fileExtention
        newNames.append(newName)
        os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("ENTER to continue")
    input()

def RemoveString():
    os.system('cls')
    print("#String Remove#")
    print("Please enter the string to remove from files:")
    stringToRemove = input()

    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print("")
    print("###############")
    print("Files found:")
    for file in onlyfiles:
        print(file)
    print("###############")
    print("")
    print("Removing string: " + stringToRemove)

    newNames = []
    for file in onlyfiles:
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = newName.replace(stringToRemove, '')
        newName = newName + fileExtention
        newNames.append(newName)
        os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("ENTER to continue")
    input()

while(True):
    os.system('cls')
    print("File Editor")
    print("")
    print("1 - Char Remove")
    print("2 - Char Replace")
    print("3 - String Remove")
    choice = input()
    if choice == "1":
        RemoveChar()
    elif choice == "2":
        ReplaceChar()
    elif choice == "3":
        RemoveString()
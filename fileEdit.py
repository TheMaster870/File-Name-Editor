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
        if file == os.path.basename(__file__):
            continue
        print(file)
    print("###############")
    print("")
    print("Removing char: " + charToRemove)

    newNames = []
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = newName.replace(charToRemove, '')
        newName = newName + fileExtention
        newNames.append(newName)
        #os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("Do you wish to continue? y/n")
    response = input()
    if response == "y":
        newNames = []
        for file in onlyfiles:
            if file == os.path.basename(__file__):
                continue
            indexOfLastDot = file.rfind('.')
            fileExtention = file[indexOfLastDot:len(file)]
            newName = file[0:indexOfLastDot]
            newName = newName.replace(charToRemove, '')
            newName = newName + fileExtention
            newNames.append(newName)
            os.rename(file, newName)
            print("Name changed: " + newName)
    else:
        print("No changes made :(")
        
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
        if file == os.path.basename(__file__):
            continue
        print(file)
    print("###############")
    print("")
    print("Replacing char: " + charToRemove + " with: " + charToInsert)

    newNames = []
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = newName.replace(charToRemove, charToInsert)
        newName = newName + fileExtention
        newNames.append(newName)
        #os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("Do you wish to continue? y/n")
    response = input()
    if response == "y":
        newNames = []
        for file in onlyfiles:
            if file == os.path.basename(__file__):
                continue
            indexOfLastDot = file.rfind('.')
            fileExtention = file[indexOfLastDot:len(file)]
            newName = file[0:indexOfLastDot]
            newName = newName.replace(charToRemove, charToInsert)
            newName = newName + fileExtention
            newNames.append(newName)
            os.rename(file, newName)
            print("Name changed: " + newName)
    else:
        print("No changes make :(")
    
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
        if file == os.path.basename(__file__):
            continue
        print(file)
    print("###############")
    print("")
    print("Removing string: " + stringToRemove)

    newNames = []
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = newName.replace(stringToRemove, '')
        newName = newName + fileExtention
        newNames.append(newName)
        #os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("Do you wish to continue? y/n")
    response = input()
    if response == "y":
        newNames = []
        for file in onlyfiles:
            if file == os.path.basename(__file__):
                continue
            indexOfLastDot = file.rfind('.')
            fileExtention = file[indexOfLastDot:len(file)]
            newName = file[0:indexOfLastDot]
            newName = newName.replace(stringToRemove, '')
            newName = newName + fileExtention
            newNames.append(newName)
            os.rename(file, newName)
            print("Name changed: " + newName)
    else:
        print("No changes made :(")
        
    print("")
    print("ENTER to continue")
    input()

def AddEnd():
    os.system('cls')
    print("#Add End#")
    print("Please enter the string to add to the ends:")
    stringToAdd = input()

    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print("")
    print("###############")
    print("Files found:")
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        print(file)
    print("###############")
    print("")
    print("Adding string: " + stringToAdd)

    newNames = []
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = newName + stringToAdd
        newName = newName + fileExtention
        newNames.append(newName)
        #os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("Do you wish to continue? y/n")
    response = input()
    if response == "y":
        newNames = []
        for file in onlyfiles:
            if file == os.path.basename(__file__):
                continue
            indexOfLastDot = file.rfind('.')
            fileExtention = file[indexOfLastDot:len(file)]
            newName = file[0:indexOfLastDot]
            newName = newName + stringToAdd
            newName = newName + fileExtention
            newNames.append(newName)
            os.rename(file, newName)
            print("Name changed: " + newName)
    else:
        print("No changes made :(")
        
    print("")
    print("ENTER to continue")
    input()

def AddStart():
    os.system('cls')
    print("#Add Start#")
    print("Please enter the string to add to the starts:")
    stringToAdd = input()

    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print("")
    print("###############")
    print("Files found:")
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        print(file)
    print("###############")
    print("")
    print("Adding string: " + stringToAdd)

    newNames = []
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = stringToAdd + newName
        newName = newName + fileExtention
        newNames.append(newName)
        #os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("Do you wish to continue? y/n")
    response = input()
    if response == "y":
        newNames = []
        for file in onlyfiles:
            if file == os.path.basename(__file__):
                continue
            indexOfLastDot = file.rfind('.')
            fileExtention = file[indexOfLastDot:len(file)]
            newName = file[0:indexOfLastDot]
            newName = stringToAdd + newName
            newName = newName + fileExtention
            newNames.append(newName)
            os.rename(file, newName)
            print("Name changed: " + newName)
    else:
        print("No changes made :(")
        
    print("")
    print("ENTER to continue")
    input()

def RemoveStart():
    os.system('cls')
    print("#Remove Start#")
    print("Please enter the the amount of chars to remove from the start:")
    numToRemove = input()

    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print("")
    print("###############")
    print("Files found:")
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        print(file)
    print("###############")
    print("")
    print("Remove num from start: " + numToRemove)

    newNames = []
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = newName[int(numToRemove):]
        newName = newName + fileExtention
        newNames.append(newName)
        #os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("Do you wish to continue? y/n")
    response = input()
    if response == "y":
        newNames = []
        for file in onlyfiles:
            if file == os.path.basename(__file__):
                continue
            indexOfLastDot = file.rfind('.')
            fileExtention = file[indexOfLastDot:len(file)]
            newName = file[0:indexOfLastDot]
            newName = newName[int(numToRemove):]
            newName = newName + fileExtention
            newNames.append(newName)
            os.rename(file, newName)
            print("Name changed: " + newName)
    else:
        print("No changes made :(")
        
    print("")
    print("ENTER to continue")
    input()

def RemoveEnd():
    os.system('cls')
    print("#Remove End#")
    print("Please enter the the amount of chars to remove from the end:")
    numToRemove = input()

    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print("")
    print("###############")
    print("Files found:")
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        print(file)
    print("###############")
    print("")
    print("Remove num from end: " + numToRemove)

    newNames = []
    for file in onlyfiles:
        if file == os.path.basename(__file__):
            continue
        indexOfLastDot = file.rfind('.')
        fileExtention = file[indexOfLastDot:len(file)]
        newName = file[0:indexOfLastDot]
        newName = newName[:-int(numToRemove)]
        newName = newName + fileExtention
        newNames.append(newName)
        #os.rename(file, newName)

    print("")
    print("###############")
    print("New File Names:")
    for file in newNames:
        print(file)
    print("###############")
    print("")
    print("Do you wish to continue? y/n")
    response = input()
    if response == "y":
        newNames = []
        for file in onlyfiles:
            if file == os.path.basename(__file__):
                continue
            indexOfLastDot = file.rfind('.')
            fileExtention = file[indexOfLastDot:len(file)]
            newName = file[0:indexOfLastDot]
            newName = newName[int(numToRemove):]
            newName = newName + fileExtention
            newNames.append(newName)
            os.rename(file, newName)
            print("Name changed: " + newName)
    else:
        print("No changes made :(")
        
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
    print("4 - Add to Start")
    print("5 - Add to End")
    print("6 - Remove from Start")
    print("7 - Remove from End")
    choice = input()
    if choice == "1":
        RemoveChar()
    elif choice == "2":
        ReplaceChar()
    elif choice == "3":
        RemoveString()
    elif choice == "4":
        AddStart()
    elif choice == "5":
        AddEnd()
    elif choice == "6":
        RemoveStart()
    elif choice == "7":
        RemoveEnd()

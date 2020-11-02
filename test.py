def listToString(namesList):
    str1 = ""
    for i in range(0, len(namesList)):
        str1 += namesList[i] + ('' if len(namesList) - 1 == i else ' ')
    return str1
a = ['Veronica', "Padilla", "Madilla", "Piston", "Gibsona"]
print(listToString(a))
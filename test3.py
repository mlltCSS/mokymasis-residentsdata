def listToString(namesList):
    x = 0
    str1 = ""
    for i in range(0, len(namesList)):
        if x < len(namesList)-1:
            str1 += namesList[i] + ('' if len(namesList) - 1 == i else ' ')
        x = x + 1
    return str1
a = ['Veronica', "Padilla", "Madilla", "Piston", "Gibsona"]
print(listToString(a))



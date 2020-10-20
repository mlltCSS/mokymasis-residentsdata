def listToString(namesList):
    str1 = ""
    x = 0
    for i in range(0, len(namesList)):
        if x < len(namesList)-1:
            str1 += namesList[i] + ' '
        elif x >= len(namesList)-1:
            str1 += namesList[i]
        x = x + 1
    #for i in range(0, len(str1)):
        #print(str1[i])
    return str1
a = ['Veronica', "Padilla", "Madilla", "Piston", "Gibsona"]
print(listToString(a))



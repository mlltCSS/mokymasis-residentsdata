def listToString(namesList):
<<<<<<< HEAD
    str1 = ""
    for i in range(0, len(namesList)):
        str1 += namesList[i] + ('' if len(namesList) - 1 == i else ' ')
=======
    x = 0
    str1 = ""
    for i in range(0, len(namesList)):
        if x < len(namesList)-1:
            str1 += namesList[i] + ('' if len(namesList) - 1 == i else ' ')
        x = x + 1
>>>>>>> c247bb342b901e76a9e7c5b3b8aa1d313634b4a2
    return str1
a = ['Veronica', "Padilla", "Madilla", "Piston", "Gibsona"]
print(listToString(a))



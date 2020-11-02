import csv

file = csv.reader(open('dataset.csv', newline=''), delimiter=',', quotechar='|')

for line in file:
    x = 0
    name = line[1].split(',')
    name = name[0].split(' ')
    surnames = name[1:]
    for surname in surnames:
        x = x + len(surname)
    if x >= 7:
        print(' '.join(name))
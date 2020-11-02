<<<<<<< HEAD
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
=======
import csv

file = csv.reader(open('dataset.csv', newline=''), delimiter=',', quotechar='|')

for line in file:
    y = line[1].split(',')
    y = y[0].split(' ')
    if len(y[1]) >= 7:
        print(" ".join(y))
>>>>>>> dc715ccee4c69b7fec0281114cdf3e396cf6e687

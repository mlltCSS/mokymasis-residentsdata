import csv

file = csv.reader(open('dataset.csv', newline=''), delimiter=',', quotechar='|')

for line in file:
    y = line[1].split(',')
    y = y[0].split(' ')
    if len(y[1]) >= 7:
        print(" ".join(y))
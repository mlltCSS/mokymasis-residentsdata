import csv
file = csv.reader(open('dataset.csv', newline=''), delimiter=',', quotechar='|')
for row in file:
    a = row[1].split(' ')
    if len(a[1]) >= 7:
        print(a[0], a[1])

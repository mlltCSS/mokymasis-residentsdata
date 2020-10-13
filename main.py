import csv
file = csv.reader(open('dataset.csv', newline=''), delimiter=',', quotechar='|')
for row in file:
    print(row[1])
    # "Martynas.Bagdonas"
    # "Marilyn Stephenson MD"
    a = row[1].split(' ')
    # ["Martynas","Bagdonas"]
    # ["Marilyn", "Stephenson", "MD"]
    b = a[1].split(...)
    # "Bagdonas"
    print(a)
    b =
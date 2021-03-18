import csv
with open('C:/Users/Andrew/Documents/Year4list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        word = ''.join(row)
        print(word)

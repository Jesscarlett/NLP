import json
import csv


data = {}
with open('D:/ScarlettBooks/Children-Stories/synonyms.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    for row in reader:
        a = row[0].replace('\xa0', '')
        b = row[1].replace('\xa0', '')
        data[a] = b

with open('D:/ScarlettBooks/Children-Stories/synonyms.json', 'w') as json_file:
    json.dump(data, json_file, indent=4, sort_keys=True)

print(data)

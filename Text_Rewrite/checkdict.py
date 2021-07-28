import json

with open('D:/ScarlettBooks/vocgov1.1/PSBjunior1.json', 'r') as dictfile:
    data = json.load(dictfile)
n = 0
for key in data:
    b = str(data[key]['definition']).lower()
    if key in b:
        n += 1
    else:
        print('ops')
        print(key)
print(n)
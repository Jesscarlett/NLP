import json

with open('D:/ScarlettBooks/vocgov1.1/PSBsenior.json', 'r') as dictfile:
    data = json.load(dictfile)
n = 0
m = 0
for key in data:
    b = str(data[key]['definition']).lower()
    if key in b:
        n += 1
    else:
        print('ops')
        print(key)
        print(data[key]['definition'])
for key in data:
    a = str(data[key]['definition']).lower()
    if "." in a:
        m += 1
    elif "?" in a:
        m += 1
    elif "!" in a:
        m += 1
    else:
        print('no .')
        print(key)
print(m)

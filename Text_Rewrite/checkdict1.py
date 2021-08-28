import json

with open('D:/ScarlettBooks/vocgov1.1/primarywords.json', 'r') as dictfile:
    data = json.load(dictfile)
n = 0
for key in data:
    value = data[key]
    if 'not found' in value:
        print(key)
        n += 1
        # print(key)
    # else:
    #     pass
print(n)

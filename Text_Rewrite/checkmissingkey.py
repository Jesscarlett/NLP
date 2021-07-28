import json

with open('D:/ScarlettBooks/Children-Stories/sentencepos.json', 'r') as file:
    data = json.load(file)
print(len(data.keys()))
newdict = data.copy()

for key, value in data.items():
    # i += 1
    # if i > 50:
    #     break
    # print(m)
    if 'sentence' in value:
        pass
    else:
        newdict.pop(key)
print(len(newdict.keys()))

with open('D:/ScarlettBooks/Children-Stories/sentencepos_new.json', 'w') as json_file:
    json.dump(newdict, json_file, indent=4, sort_keys=True)


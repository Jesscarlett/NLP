import json
from nltk.corpus import wordnet

i = 0
j = 0
with open('D:/ScarlettBooks/Dictionary/DZ.json', 'r') as file:
    data = json.load(file)
    key_list = list(data.keys())
    # print(len(key_list))
    for key in key_list:
        print(key)
        print(data[key]['MEANINGS'])
        if len(data[key]['MEANINGS']) < 2:
            try:
                syn = wordnet.synsets(key)[0]
                print('[Meaning] - ' + syn.definition())
                data[key]['MEANINGS']['1'] = syn.definition()
                j += 1
            except IndexError:
                data[key]['MEANINGS']['1'] = 'Not available'
                i += 1
        else:
            pass

print(i)
print(j)
print(len(key_list))
with open('D:/ScarlettBooks/Dictnew/DZ.json', 'w') as json_file:
    json.dump(data, json_file, sort_keys=True)
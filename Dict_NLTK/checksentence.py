import json

with open("D:/ScarlettBooks/story-json/sentencepos.json") as file:
    example3_dict = json.load(file)
n = 0
for key in example3_dict.keys():
    if key in example3_dict[key]['sentence'].lower():
        pass
    elif key[0:3] in example3_dict[key]['sentence'].lower():
        pass
    else:
        n += 1
        print(key)
        print(example3_dict[key]['sentence'])
print(n)


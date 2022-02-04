import json

with open("D:/ScarlettBooks/story-json/sentence.json") as file:
    sentence_dict = json.load(file)
    new_dict = sentence_dict.copy()
    i = 0
    for key in sentence_dict:
        verb_words = sentence_dict[key]['verbs']
        ad_words = sentence_dict[key]['others']
        if (len(verb_words) < 2) or (len(ad_words) < 2):
            i += 1
print(i)


with open('D:/ScarlettBooks/story-json/sentence1.json', 'w') as json_file:
    json.dump(new_dict, json_file, indent=4, sort_keys=True)

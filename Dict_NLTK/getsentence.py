import json

with open("D:/ScarlettBooks/story-json/PSBsenior.json") as file:
    example1_dict = json.load(file)

with open("D:/ScarlettBooks/story-json/PSBjunior.json") as file:
    example2_dict = json.load(file)

with open("D:/ScarlettBooks/story-json/sentencepos.json") as file:
    example3_dict = json.load(file)

    key_word = 'astrology'
    k = key_word.lower()
    if k in example1_dict.keys():
        print('found it')
        print(example1_dict[k]['definition'])
        sentence_list = example1_dict[k]['definition'].split(": ", 1)
        sentence = sentence_list[-1]
        print(sentence)
    elif k in example2_dict.keys():
        sentence_list = example2_dict[k]['definition'].split(": ", 1)
        sentence = sentence_list[-1]
        print(sentence)
    elif k in example3_dict.keys():
        sentence = example3_dict[k]['sentence']
        print('sentence')
        print(sentence)
    else:
        sentence = ""



import random
import nltk
import json
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

filename = 'D://ScarlettBooks//Top100kidsbooks//Treasure-Island-by-Robert-Louis-Stevenson-2.txt'
story_dict = {}
para = ""
p = 0
with open(filename, encoding="utf-8") as file:
    for i, line in enumerate(file):
        if (line == '\n') or (len(line) < 3) or (any(map(str.isdigit, line)) == True):
            if (len(para) > 140) and (len(para) < 420) and ('   ' not in para):
                i += 1
                k = "TI" + str(p)
                story_dict[k] = para.replace("\\", "")
                p += 1
                para = ""
            else:
                para = ""
        else:
            para += line.replace('\n', ' ')
            # print(para)

for key in story_dict:
    punkt_params = PunktParameters()
    punkt_params.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e'])
    tokenizer = PunktSentenceTokenizer(punkt_params)
    tokens = tokenizer.tokenize(story_dict[key])
    for t in tokens:
        if 'quick' in t:
            # print(type(t))
            t.rstrip()
            print(t)
            break


# with open('D:/ScarlettBooks/story-json/test.json', 'w') as json_file:
#     json.dump(story_dict, json_file, indent=4, sort_keys=True)
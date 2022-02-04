import random
import nltk
import json
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

filename = 'D://ScarlettBooks//story-json//mergedstory.txt'
story_dict = {}
para = ""
p = 10000
with open(filename, encoding="utf-8") as file:
    for i, line in enumerate(file):
        if (line == '\n') or (len(line) < 3) or (any(map(str.isdigit, line)) == True):
            if (len(para) > 200) and (len(para) < 400) and ('   ' not in para) and ('"' not in para) \
                    and ('--' not in para) and ("(" not in para) and ("_" not in para)\
                    and (";" not in para) and (":" not in para) and ("'" not in para) \
                    and ("kill" not in para) and ("killed" not in para) and ("murder" not in para)\
                    and (para[0].isupper() == True) and (para[-1].islower() == False):
                i += 1
                # k = "TI" + str(p)
                story_dict[p] = para.replace("\\", "")
                p += 1
                para = ""
            else:
                para = ""
        else:
            para += line.replace('\n', ' ')
            # print(para)

# for key in story_dict:
#     punkt_params = PunktParameters()
#     punkt_params.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e'])
#     tokenizer = PunktSentenceTokenizer(punkt_params)
#     tokens = tokenizer.tokenize(story_dict[key])
#     for t in tokens:
#         if 'quick' in t:
#             # print(type(t))
#             t.rstrip()
#             print(t)
#             break


with open('D:/ScarlettBooks/story-json/test_simplified.json', 'w') as json_file:
    json.dump(story_dict, json_file, indent=4, sort_keys=True)
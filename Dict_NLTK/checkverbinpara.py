import nltk
import json
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

sentence_dict = {}
with open("D:/ScarlettBooks/story-json/test_simplified.json") as file:
    story_dict = json.load(file)
n = 0
i = 10000
master_list = []
for key in story_dict:
    # print(story_dict[key])
    n += 1
    v = 0
    punkt_params = PunktParameters()
    punkt_params.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e'])
    tokenizer = PunktSentenceTokenizer(punkt_params)
    sentences = tokenizer.tokenize(story_dict[key])
    verb_list = []
    adjective_list =[]
    for sen in sentences:
        words = nltk.word_tokenize(sen)
        pos_pairs = nltk.pos_tag(words)
        # print(pos_pairs)
        for a, b in pos_pairs:
            if (len(a) > 4) and ('-' not in a):
                if 'VB' in b:
                    verb_list.append(a)
                elif ('JJ' in b) or ('RB' in b):
                    adjective_list.append(a)
    if (len(list(set(verb_list))) > 1) and (len(list(set(adjective_list))) > 1):
        i += 1
        sentence_dict[i] = {}
        sentence_dict[i]['l'] = str(story_dict[key])
        sentence_dict[i]['v'] = list(set(verb_list))
        sentence_dict[i]['o'] = list(set(adjective_list))
        print(sentence_dict[i])
    else:
        pass
#     master_list += word_list
#     if n > 500:
#         break
# master_list_final = list(set(master_list))
# print(master_list_final)
# print(len(master_list_final))
with open('D:/ScarlettBooks/story-json/sentence.json', 'w') as json_file:
    json.dump(sentence_dict, json_file, sort_keys=True)

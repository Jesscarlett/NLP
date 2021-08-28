import json

with open("D:/ScarlettBooks/vocgov1.1/sentencepos_old.json") as file:
    word_dict = json.load(file)
out_file = open("D:/ScarlettBooks/vocgov1.1/sentencepos.json", "w")
json.dump(word_dict, out_file, sort_keys=False)
out_file.close()
# #     pairs = word_dict.items()
# # for key, value in pairs:
#     print(x + ": " + word_dict[x])

# word = string.upper()
# if word in word_dict:
#     print('yes')
#     meaning = word_dict.get(string)
#     print(meaning)
    # full_meaning = meaning.get('MEANINGS')
    # # first_pair = next(iter((full_meaning.items())))
    # # print(first_pair)
    # first_n_pair = list(full_meaning.items())[:2]
    # print(first_n_pair)
    # # brief_meaning = list(full_meaning)[0]
    # m = str(first_n_pair)
    # m = meaning.translate(str.maketrans({'{': None,
    #                                           '}': None,
    #                                           "[": None,
    #                                           "]": None,
    #                                           "'": None,
    #                                           "'": None,
    #                                           "(": None,
    #                                           ")": None}))
    # # synonyms = meaning.get('SYNONYMS')
    # # word_synonym = str(synonyms).translate(str.maketrans({'{': None,
    # #                                                       '}': None,
    # #                                                       "[": None,
    # #                                                       "]": None,
    # #                                                       "'": None,
    # #                                                       "'": None,
    # #                                                       "(": None,
    # #                                                       ")": None}))
    # # print(word_synonym)
    # print(m)
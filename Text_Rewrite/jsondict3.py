import json

string = 'star'
x = string.lower()
with open("D:/ScarlettBooks/Children-Stories/dictionary_compact.json") as file:
    word_dict = json.load(file)
#     pairs = word_dict.items()
# for key, value in pairs:
    print(x + ": " + word_dict[x])

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
import json

string = 'beautifully'
x = string[0].upper()
with open(f"E:/Downloads/data/D{x}.json") as file:
    word_dict = json.load(file)
word = string.upper()
if word in word_dict:
    print('yes')
    meaning = word_dict.get(word)
    print(meaning)
    full_meaning = meaning.get('MEANINGS')
    # first_pair = next(iter((full_meaning.items())))
    # print(first_pair)
    first_n_pair = list(full_meaning.items())[:2]
    print(first_n_pair)
    # brief_meaning = list(full_meaning)[0]
    m = str(first_n_pair)
    word_meaning = m.translate(str.maketrans({'{': None,
                                              '}': None,
                                              "[": None,
                                              "]": None,
                                              "'": None,
                                              "'": None,
                                              "(": None,
                                              ")": None}))
    synonyms = meaning.get('SYNONYMS')
    word_synonym = str(synonyms).translate(str.maketrans({'{': None,
                                                          '}': None,
                                                          "[": None,
                                                          "]": None,
                                                          "'": None,
                                                          "'": None,
                                                          "(": None,
                                                          ")": None}))
    # print(word_synonym)

    print('MEANINGS: ' + word_meaning + '. | SYNONYMS: ' + word_synonym)

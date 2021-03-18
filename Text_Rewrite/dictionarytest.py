from PyDictionary import PyDictionary
dictionary = PyDictionary()

dictionary = PyDictionary("tag")

# print(dictionary.printMeanings())
# print(dictionary.getMeanings())
# print(dictionary.getSynonyms())
val_list = dictionary.getMeanings().values()
for val in val_list:
    print(val)
    print(type(val))
    parts = val.keys()
    print(parts)
    pos = []
    for part in parts:
        pos.append(part)
    print(pos)






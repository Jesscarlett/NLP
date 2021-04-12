from nltk.corpus import wordnet
from nltk.corpus import framenet
from datamuse import datamuse
api = datamuse.Datamuse()

w = 'tell'

syn = wordnet.synsets(w)[0]
print(syn.name())
print(syn.definition())
example = str(syn.examples()).replace('["', '')
print(example)
# word_synonym = api.words(rel_syn=w, max=5)
# word_antonym = api.words(rel_ant=w, max=5)
# print(w.tagged_words(tagset='universal'))
# print(word_synonym)
# print(word_antonym)

# print(syn.hypernyms())
# print(syn.hypernyms()[0].hyponyms())
# print(syn.root_hypernyms())
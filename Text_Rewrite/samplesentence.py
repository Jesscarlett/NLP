import random
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

filename = 'D://ScarlettBooks//Top100kidsbooks//Treasure-Island-by-Robert-Louis-Stevenson-2.txt'
word = 'home'
word1 = word + ' '
word2 = word + ','
word3 = word + '.'
i = 0
line_list = []
with open(filename, encoding="utf-8") as file:
    try:
        for i, line in enumerate(file):
            i += 1
            if (word1 or word2 or word3) in line:
                print(line)
                line_list.append(i)
            if i == 468:
                print(line)
        print(line_list)
        n = random.choice(line_list)
        print(n)
    except IndexError:
        print('cannot find the word')

s = ""
with open(filename, encoding="utf-8") as file:
    for i, line in enumerate(file):
        if i > n-8:
            s += line
        if i == n+5:
            break
# print(s)

punkt_params = PunktParameters()
punkt_params.abbrev_types = set(['Dr', 'vs', 'Mr', 'Mrs', 'Prof', 'inc'])
tokenizer = PunktSentenceTokenizer(punkt_params)
tokens = tokenizer.tokenize(s)
for t in tokens:
    if word in t:
        print(type(t))
        t.rstrip()
        print(t)
        break


import random
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

filename = 'D:/ScarlettBooks/outbooks/tokenizedsentences.txt'
first_word = 'green'
second_word = 'grass'
fword1 = ' ' + first_word + ' '
fword2 = ' ' + first_word + ','
fword3 = ' ' + first_word + '.'
sword1 = ' ' + second_word + ' '
sword2 = ' ' + second_word + ','
sword3 = ' ' + second_word + '.'

i = 0
line_list = []
with open(filename, encoding="utf-8") as file:
    try:
        for i, line in enumerate(file):
            i += 1
            if (fword1 or fword2 or fword3 or sword1 or sword2 or sword3) in line:
                # print(line)
                line_list.append(i)
            else:
                pass
            # if i == 468:
            #     print(line)
        # print(line_list)
        # n = random.sample(line_list, 10)
        n = line_list
        # print(n)
    except IndexError:
        print('cannot find the word')

for a in n:
    s = ""
    with open(filename, encoding="utf-8") as file:
        for i, line in enumerate(file):
            if i > a-8:
                s += line
            if i == a+5:
                break
    # print(s)
    s.replace('\n', '')
    punkt_params = PunktParameters()
    punkt_params.abbrev_types = set(['Dr', 'vs', 'Mr', 'Mrs', 'Prof', 'inc'])
    tokenizer = PunktSentenceTokenizer(punkt_params)
    tokens = tokenizer.tokenize(s)
    for t in tokens:
        if first_word in t:
            if second_word in t:
                print(type(t))
                t.strip()
                t = ' '.join(t.splitlines())
                if '"' in t or '-' in t or '(' in t or ']' in t or "'" in t:
                    pass
                elif t[0].islower() or t[1].isupper():
                    pass
                elif len(t) < 100 or len(t) > 400:
                    pass
                else:
                    print(t)
            else:
                pass
        else:
            pass


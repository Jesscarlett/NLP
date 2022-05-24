import random

filename = 'D:/ScarlettBooks/outbooks/tokenizedsentences.txt'
first_word = 'barefoot'
second_word = ''
fword1 = ' ' + first_word + ' '
fword2 = ' ' + first_word + ','
fword3 = ' ' + first_word + '.'
sword1 = ' ' + second_word + ' '
sword2 = ' ' + second_word + ','
sword3 = ' ' + second_word + '.'

with open(filename, encoding="utf-8") as file:
    for i, line in enumerate(file):
        if first_word in line:
            if second_word in line:
                print(i)
                print(line)
            else:
                pass
        else:
            pass

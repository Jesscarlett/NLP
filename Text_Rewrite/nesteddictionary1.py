import csv
import json
import re

word_list = []
word_list1 = []
dict = {}
meaning = []
with open('D:/ScarlettBooks/vocgov1.1/juniorwordlist1.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        word = ''.join(row)
        word_list.append(word)
print(word_list)

with open('D:/ScarlettBooks/vocgov1.1/juniorwordlist2.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        word = ''.join(row)
        word_list1.append(word)
print(word_list1)

word_list2 = [i for i in word_list1 if i not in word_list]
print(word_list2)
print(len(word_list2))

with open('D:/ScarlettBooks/vocgov1.1/PSBjunior.json', 'r') as dictfile:
    data = json.load(dictfile)
newdict = data.copy()
print(newdict)
print(len(newdict.keys()))

with open('D:/ScarlettBooks/vocgov1.1/juniorwordlist2-meaning.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    n = 0
    # i = 0
    for row in reader:
        mean = ''.join(row)
        # print(mean)
        # i += 1
        if '(say' not in mean:
            if mean not in word_list2:
                # print('no')
                n = 1
                pass
            else:
                word = str(mean)
                n = 0
                # print(word)
                newdict[word] = {}
                pass
        else:
            if n == 0:
                result = re.split('[)]+', mean, maxsplit=1)
                # print(result)
                newdict[word] = {}
                newdict[word]['pronunciation'] = str(result[0] + ')')
                newdict[word]['definition'] = str(result[1])
                # print(newdict[word])
            else:
                n = 0
                pass


#         elif n == 1:
#             dict[word] = {}
#             dict[word]['pronunciation'] = mean
#             n += 1
#             pass
#         elif n == 2:
#             d = str(mean)
#             n += 1
#             pass
#         elif n > 2:
#             if mean in word_list:
#                 dict[word]['definition'] = d
#                 n = 0
#                 word = str(mean)
#                 n += 1
#             else:
#                 d = d + ' ' + mean
#                 n += 1
#         # if i > 500:
#         #     break
# dict[word]['definition'] = d
print(len(newdict.keys()))
out_file = open("D:/ScarlettBooks/vocgov1.1/PSBjunior1.json", "w")
json.dump(newdict, out_file, sort_keys=False)
out_file.close()
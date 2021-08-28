import csv
import json
import re

word_list = []
word_list1 = []
dict = {}
meaning = []
with open('D:/ScarlettBooks/vocgov1.1/seniorwordlist1.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        word = ''.join(row)
        word_list.append(word)
print(word_list)

with open('D:/ScarlettBooks/vocgov1.1/seniorwordlist2.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        word = ''.join(row)
        word_list1.append(word)
print(word_list1)

word_list2 = [i for i in word_list1 if i not in word_list]
print(word_list2)
print(len(word_list2))

with open('D:/ScarlettBooks/vocgov1.1/PSBsenior_old.json', 'r') as dictfile:
    data = json.load(dictfile)
newdict = data.copy()
print(newdict)
print(len(newdict.keys()))

with open('D:/ScarlettBooks/vocgov1.1/seniorwordlist2-meaning.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    n = 0
    for row in reader:
        mean = ''.join(row)
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

print(len(newdict.keys()))
out_file = open("D:/ScarlettBooks/vocgov1.1/PSBsenior.json", "w")
json.dump(newdict, out_file, indent=4, sort_keys=False)
out_file.close()
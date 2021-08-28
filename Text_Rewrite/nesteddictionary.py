import csv
import json

word_list = []
dict = {}
meaning = []
with open('D:/ScarlettBooks/vocgov1.1/seniorwordlist.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        word = ''.join(row)
        word_list.append(word)
print(word_list)
print(len(word_list))

with open('D:/ScarlettBooks/vocgov1.1/seniorwordlist1.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    n = 0
    # i = 0
    for row in reader:
        mean = ''.join(row)
        print(mean)
        # i += 1
        if n == 0:
            if mean in word_list:
                print('yes')
                n += 1
                word = str(mean)
                dict[word] = {}
                pass
            else:
                pass
        elif n == 1:
            dict[word] = {}
            dict[word]['pronunciation'] = mean
            n += 1
            pass
        elif n == 2:
            d = str(mean)
            n += 1
            pass
        elif n > 2:
            if mean in word_list:
                dict[word]['definition'] = d
                n = 0
                word = str(mean)
                n += 1
            else:
                d = d + ' ' + mean
                n += 1
        # if i > 500:
        #     break
dict[word]['definition'] = d
# print(dict)
out_file = open("D:/ScarlettBooks/vocgov1.1/PSBsenior_old.json", "w")
json.dump(dict, out_file, indent=4, sort_keys=False)
out_file.close()
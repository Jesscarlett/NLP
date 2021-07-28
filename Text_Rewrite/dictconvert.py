import json

with open('D:/ScarlettBooks/Children-Stories/test.json', 'r') as file:
    data = json.load(file)
dict_list = []
i = 1
n = 1
meaning = ""
term = ""
with open('D:/ScarlettBooks/Children-Stories/Pocket-Oxford-English-Dictionary.txt', encoding="utf8") as file:
    for i, line in enumerate(file):
        i += 1
        n += 1
        if 'Back New Search' in line:
            n = 0
        if n < 4:
            pass
        elif n == 4:
            print(line)
            term = line.strip()
            data.update({term: ' '})
        elif n > 4:
            if 'ORIGIN' in line:
                pass
            elif line == '\n':
                pass
            else:
                meaning += str(line.strip() + ' ')
                print(meaning)
        if '* * *' in line:
            m = meaning.replace("* * *", "")
            data[term] = m
            meaning = ""
        # if i > 1111000:
            # break

# my_dict = {key: None for key in dict_list}
with open('D:/ScarlettBooks/Children-Stories/fulldict.json', 'w') as json_file:
    json.dump(data, json_file, indent=4, sort_keys=True)

import json
import random

new_dict = {}
# word = 'home'

with open("D:/ScarlettBooks/Children-Stories/quotes_old.json") as file:
    quotes_dict = json.load(file)
    # i = random.randint(1, 5421)
    # k = str(i)
    # print(quotes_dict[k]['T'])
    # print('--- ' + quotes_dict[k]['A'])
    # for d in quotes_dict.values():
    #     # print(type(d))
    #     # print(d['T'])
    #     if word in str(d['T']):
    #         print(d['T'])
    #     else:
    #         pass

    for di in quotes_dict:
        print(type(di))
        print(di['T'])


    # i = 0
    # for d in quotes_dict:
    #     # print(key)
    #     i += 1
    #     # print(d)
    #     # print(type(d))
    #     new_dict[i] = d

        # for k in d:
        #     print(type(k))


# with open('D:/ScarlettBooks/Children-Stories/quotes1.json', 'w') as json_file:
#     json.dump(new_dict, json_file, sort_keys=True)


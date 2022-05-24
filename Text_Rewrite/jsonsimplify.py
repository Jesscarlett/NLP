import json
import csv
import random

new_dict = {}
quotes_list = []
word = 'sparkling'
i = 0
### replace empty string with unknown ###
# with open("D:/ScarlettBooks/Children-Stories/quotes.json") as file:
#     quotes_dict = json.load(file)
#     for key, value in quotes_dict.items():
#         if len(value['A']) == 0:
#             quotes_dict[key]['A'] = 'unknown'
#             # print(quotes_dict[key])
#             i += 1
#         else:
#             pass
# print(i)
# with open('D:/ScarlettBooks/Children-Stories/quotes4.json', 'w') as json_file:
#     json.dump(quotes_dict, json_file, sort_keys=False)





#### simplify dictionary ####
# with open("D:/ScarlettBooks/Children-Stories/quotes.json") as file:
#     quotes_dict = json.load(file)
#     quotes_new_dict = quotes_dict.copy()
#     print(len(quotes_dict))
#     for key, quote in quotes_dict.items():
#         if quote['C'].lower() == 'movies':
#             del quotes_new_dict[key]
#         elif quote['C'].lower() == 'sex':
#             del quotes_new_dict[key]
#         elif quote['C'].lower() == 'music':
#             del quotes_new_dict[key]
#         elif len(quote['Q']) > 140:
#             del quotes_new_dict[key]
#         elif len(quote['Q']) < 30:
#             del quotes_new_dict[key]
#         else:
#             pass
#     print(len(quotes_new_dict))
#     i = 1
#     for v in quotes_new_dict.values():
#         new_dict[str(i)] = v
#         i += 1
#     print(new_dict)
#
# with open('D:/ScarlettBooks/Children-Stories/quotes4.json', 'w') as json_file:
#     json.dump(new_dict, json_file, sort_keys=False)


#### random range ####
with open("D:/ScarlettBooks/Children-Stories/quotes.json") as file:
    quotes_dict = json.load(file)
    i = random.randint(2, 23144)
    n = 0
    for x in range(i, 23145):
        if word in quotes_dict[str(x)]['Q'].lower():
            quotes_list.append(quotes_dict[str(x)]['Q'] + ' --- ' + quotes_dict[str(x)]['A'])
            n += 1
            if n > 2:
                break
            else:
                pass
        else:
            pass

    for y in range(1, i):
        if n > 2:
            break
        else:
            if word in quotes_dict[str(y)]['Q'].lower():
                quotes_list.append(quotes_dict[str(y)]['Q'] + ' --- ' + quotes_dict[str(x)]['A'])
                n += 1
            else:
                pass
print(quotes_list)


    # for quote in quotes_dict.values():
    #     # print(type(quote))
    #     if word in quote['Q']:
    #         print(quote['Q'] + '\n' + '---' + quote['A'])
    #         n += 1
    #         if n > 2:
    #             break
    #     else:
    #         pass





# n = 0
# with open('D:/ScarlettBooks/Children-Stories/QuotesDatabase.csv', encoding='utf-8-sig') as csv_file:
#     # reader = csv.DictReader(csv_file, fieldnames=None, restkey=None, restval=None)
#     reader = (line.replace('\n', '') for line in csv_file)
#     counter = 1
#     for row in csv.DictReader(reader):
#         # print(dict(row))
#         # print(type(row))
#         new_dict[str(counter)] = dict(row)
#         quotes_list.append(dict(row)['Q'])
#         counter += 1
#
# # with open("D:/ScarlettBooks/Children-Stories/quotes.json") as file:
# #     quotes_dict = json.load(file)
# counter = counter - 1
# # print(new_dict[str(counter)]['Q'])
#
# with open("D:/ScarlettBooks/Children-Stories/quotes.json") as file:
#     quotes_dict = json.load(file)
#     for i in range(1, 5421):
#         if quotes_dict[str(i)]['T'] in quotes_list:
#             # print(quotes_dict[str(i)]['T'])
#             n += 1
#             pass
#         else:
#             counter += 1
#             new_dict[str(counter)] = {}
#             new_dict[str(counter)]['Q'] = quotes_dict[str(i)]['T']
#             new_dict[str(counter)]['A'] = quotes_dict[str(i)]['A']
#             new_dict[str(counter)]['C'] = "general"
#             quotes_list.append(quotes_dict[str(i)]['T'])
#
# print(n)
# with open('D:/ScarlettBooks/Children-Stories/quotes4.json', 'w') as json_file:
#     json.dump(new_dict, json_file, sort_keys=False)

# with open('D:/ScarlettBooks/Children-Stories/quotes1.json', 'r') as json_file:
#     quote_dict = json.load(json_file)
#     e = 0
#     for q in quote_dict.keys():
#         e += 1
#     print(e)

import json
import random
with open("D:/ScarlettBooks/story-json/sentence.json") as file:
    sentence_dict = json.load(file)

i = random.randint(10001, 14111)
key = str(i)
words = sentence_dict[key]['wds']
para = sentence_dict[key]['sen']
para_answer = sentence_dict[key]['sen']
random.shuffle(words)
n = 0
m = 0
word_list = []
for word in words:
    print(word)
    n += 1
    para = para.replace(word, '-(x)-', 1)
    word_list.append(word)
    if n > 4:
        break

for x in range(1, 6):
    para = para.replace('(x)', f'({x})', 1)

order = []
for w in word_list:
    m += 1
    order_num = para_answer.find(w)
    order.append(order_num)

order_list = order.copy()
order_list.sort()

num = ''
for index in order_list:
    num += str(order.index(index) + 1)

print(para)
print(sentence_dict[key]['sen'])
print(word_list)
print(order)
print(order_list)
print(num)
# print(type(sentence_dict[key]['wds']))

# print(i)
# print(sentence_dict[key])

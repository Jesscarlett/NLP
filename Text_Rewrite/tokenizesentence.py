import nltk
from nltk.tokenize import sent_tokenize
import os

# Folder Path
path = "D:/ScarlettBooks/Top100teenbooks"

# Change the directory
os.chdir(path)
for file in os.listdir():
    # Check whether file is in text format or not
    filename = f"{path}/{file}"
    lines = []
    with open(filename, encoding="utf-8") as file:

        for line in file:
            if '(' in line or ']' in line or '[' in line or '*' in line or 'Chapter' in line or '_' in line or 'CHAPTER' in line or 'LoyalBooks' in line:
                pass
            else:
                lines.append(line.strip())
    raw_text = ' '.join(lines).replace('\n', '')
    text = raw_text.strip()
    print(type(sent_tokenize(text)))
    for p in sent_tokenize(text):
        if len(p) < 100 or len(p) > 400:
            pass
        elif p[0].islower() or p[1].isupper():
            pass
        else:
            with open('D:/ScarlettBooks/outbooks/tokenizedsentences.txt', 'a', encoding="utf-8") as file:
                file.write(p)
                file.write('\n')




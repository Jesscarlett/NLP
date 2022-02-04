import glob
import os

with open('D:/ScarlettBooks/story-json/mergedstory.txt', 'w', encoding='utf-8') as outfile:

    for f in glob.glob('D:/ScarlettBooks/story-json/*.txt'):
        with open(f, 'r', encoding='utf-8', errors='ignore') as openfile:
            outfile.write(openfile.read())
        outfile.write('\n')

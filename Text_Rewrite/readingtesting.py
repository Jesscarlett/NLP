import bs4
import requests
from bs4 import BeautifulSoup as bs
from urllib import request
import re
import os
import urllib
import csv

#

path = 'D:\\ScarlettBooks\\temp'
files = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))
print(files)

for item in files:
    line_number = 0
    with open(item, 'r', encoding="utf8") as text_file:
        for sentence in text_file:
            line_number += 1
            if "Chapter I" in sentence:
                print(sentence)
                print(line_number)
                print(item)
                break
            elif "Chapter 1" in sentence:

                print(sentence)
                print(line_number)
                print(item)
                break
            elif "CHAPTER I" in sentence:

                print(sentence)
                print(line_number)
                print(item)
                break
            else:
                continue



import bs4
import requests
from bs4 import BeautifulSoup as bs
from urllib import request
import random
import re
import os
import urllib
from nltk.corpus import wordnet
from datamuse import datamuse
from docx import Document
from googletrans import Translator
import csv

id_list = ['gexv2row1', 'gexv2row2']
doc_path = "C:/Users/Andrew/Documents/AUS-Grade4-Vocab-excercise.docx"
n = 0

url_word = 'crabby'
# url = "https://www.dictionary.com/browse/" + word
url = "https://tangorin.com/sentences?search=" + url_word
page_html = request.urlopen(url).read()
page_soup = bs(page_html, "html.parser")
# random_id = random.choice(id_list)
# my_divs = page_soup.find_all("p", {"class": 'one-click-content css-fr4dvi-Sentence e15kc6du2'})
my_divs = page_soup.find_all("dd", {"class": 's-en'})
if len(my_divs) < 10:
    print('error')
else:
    for my_div in my_divs:
        n = n + 1
        p_str = my_div.text.strip()
        question = p_str.replace(url_word, '______________')
        if n < 2:
            print(question)
        else:
            break


import bs4
import requests
from bs4 import BeautifulSoup as bs
from urllib import request
import re
import os
import urllib
from nltk.corpus import wordnet
from datamuse import datamuse
from docx import Document
import csv
from PyDictionary import PyDictionary
dictionary = PyDictionary()
api = datamuse.Datamuse()

word = 'tricky'
url = "https://eng.ichacha.net/zaoju/" + word + ".html"
page_html = request.urlopen(url).read()
page_soup = bs(page_html, "html.parser")
my_divs = page_soup.find_all("li", {"style": "text-align:left"})
n = 0
for div in my_divs:
    div_str = str(div.text)
    n = n + 1
    if n < 3:
        print(div_str)


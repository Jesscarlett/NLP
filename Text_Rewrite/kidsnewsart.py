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
from urllib.request import Request, urlopen
dictionary = PyDictionary()
api = datamuse.Datamuse()


word = 'science'
page_url = "https://www.kidsnews.com.au/history/footy-legend-tom-harley-learns-of-his-grandfathers-great-wwii-escape/news-story/eaa87edb35082a2e5cd2a7866c6b5b0c"
# page_html = request.urlopen(url).read()
req = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
page_html = urlopen(req).read()
page_soup = bs(page_html, "html.parser")
my_hs = page_soup.find_all("h1", {"class": "headline"})
my_ps = page_soup.find_all("p", {"class": "capi-html"})
n = 0
# urls = []
# print(my_hs)
# print(my_ps)
for h in my_hs:
    h_str = str(h.text)
    print(h_str)
    print(' ')
for p in my_ps:
    p_str = str(p.text)
    print(' ')
    print(p_str)
    if p_str == 'GLOSSARY':
        break
    else:
        continue


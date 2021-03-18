import bs4
import requests
from bs4 import BeautifulSoup as bs
from urllib import request
import re
import os
import urllib

word = 'else'

url2 = "https://thesaurus.yourdictionary.com/" + word
page_html2 = request.urlopen(url2).read()
page_soup2 = bs(page_html2, "html.parser")
my_syns = page_soup2.find_all("a", {"class": "synonym-link"})
for syn in my_syns:
    syn_str = str(syn.text)
    print(syn_str)
import bs4
import requests
from bs4 import BeautifulSoup as bs
from urllib import request
import urllib.request
import random
import re
import os
import urllib
from nltk.corpus import wordnet
from datamuse import datamuse
from docx import Document
from googletrans import Translator
import csv

for i in range(1, 10):
    url = "https://www.shortkidstories.com/story/page/" + str(i) + "/?story_category&age-range=teen&authors&reading-time"
    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0)'}
    req = urllib.request.Request(url, headers=hdr)
    page_html = urllib.request.urlopen(req).read()
    page_soup = bs(page_html, "html.parser")
    my_divs = page_soup.find_all("a", {"class": 'sks-story-link'})
    # print(i)

    for my_div in my_divs:
        # print(my_div)
        link = my_div.attrs.get("href")
        # with open('D:/ScarlettBooks/Children-Stories/storylist.csv', 'w', newline='') as file:
        #     thewriter = csv.writer(file)
        #     thewriter.writerow(link)
        print(link)



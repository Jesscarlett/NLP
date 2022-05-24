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

word = 'bright'
syn = wordnet.synsets(word)
print(syn)

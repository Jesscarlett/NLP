from textblob import TextBlob
import nltk
from textblob import Word
import sys
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

with open (r'C:\Users\Andrew\Documents\Vocab\blank\wave.txt', encoding='utf8') as f:
    string = f.read()
    print(string)
    word_list = string.split()
    number_of_words = len(word_list)
    print(number_of_words)
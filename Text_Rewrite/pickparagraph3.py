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
import glob

# CC coordinating conjunction
# CD cardinal digit
# DT determiner
# EX existential there (like: “there is” … think of it like “there exists”)
# FW foreign word
# IN preposition/subordinating conjunction
# JJ adjective ‘big’
# JJR adjective, comparative ‘bigger’
# JJS adjective, superlative ‘biggest’
# LS list marker 1)
# MD modal could, will
# NN noun, singular ‘desk’
# NNS noun plural ‘desks’
# NNP proper noun, singular ‘Harrison’
# NNPS proper noun, plural ‘Americans’
# PDT predeterminer ‘all the kids’
# POS possessive ending parent‘s
# PRP personal pronoun I, he, she
# PRP$ possessive pronoun my, his, hers
# RB adverb very, silently,
# RBR adverb, comparative better
# RBS adverb, superlative best
# RP particle give up
# TO to go ‘to‘ the store.
# UH interjection errrrrrrrm
# VB verb, base form take
# VBD verb, past tense took
# VBG verb, gerund/present participle taking
# VBN verb, past participle taken
# VBP verb, sing. present, non-3d take
# VBZ verb, 3rd person sing. present takes
# WDT wh-determiner which
# WP wh-pronoun who, what
# WP$ possessive wh-pronoun whose
# WRB wh-abverb where, when

# doc_path = "D:/ScarlettBooks/Children-Stories/LittlePrincess-Reading-Vocab-exercise.docx"
# my_doc = Document(doc_path)

for f in glob.glob('D:/ScarlettBooks/Children-Stories/*.txt'):
    file = None
    with open(f, 'r', encoding="utf-8") as openfile:
        i = 0
        e = 10
        for lineno, line in enumerate(openfile):
            i += 1
            if lineno % 45 == 0:
                e += 1
                if file:
                    file.close()
                # if len(line) > 2:
                #     r = e - 1
                #     file_name = 'D:/ScarlettBooks/Children-Stories/Little-Women/{}.txt'.format(r)
                #     file = open(file_name, 'a', encoding="utf-8")
                # else:
                file_name = 'D:/ScarlettBooks/Children-Stories/The-Secret-Zoo/{}.txt'.format(e)
                file = open(file_name, 'a', encoding="utf-8")
                file.write(line)
            else:
                file_name = 'D:/ScarlettBooks/Children-Stories/The-Secret-Zoo/{}.txt'.format(e)
                file = open(file_name, 'a', encoding="utf-8")
                file.write(line)
        if file:
            file.close()
                # if line != '\n':
                #     with open('D:/ScarlettBooks/Children-Stories/Little-Women/{}.txt'.format(e), 'a', encoding="utf-8") as writefile:
                #         writefile.write(line)
                # else:
                #     e += 1
                #     break

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

doc_path = "D:/ScarlettBooks/Children-Stories/LittlePrincess-Reading-Vocab-exercise.docx"
my_doc = Document(doc_path)

for f in glob.glob('D:/ScarlettBooks/Children-Stories/*.txt'):
    with open(f, 'r', encoding="utf-8") as openfile:
        i = 0
        j = 0
        numbers_list = [0]
        for line in openfile:
            j += 1
            if line == '\n':
                numbers_list.append(j)
                a = int(numbers_list[-1]) - int(numbers_list[-2])
                if a < 7:
                    numbers_list.pop()
                else:
                   pass
            else:
                pass
            if len(numbers_list) > 50:
                break
        numbers_list.pop(0)
        print(numbers_list)
        for n, number in enumerate(numbers_list):
            if n > 3:
                break
            else:
                m = 0
                for line in openfile:
                    m += 1
                    if m > int(number):
                        print(line)
                        my_doc.add_paragraph(line)
                        if m > int(number) + 20 and line == '\n':
                            break
                        else:
                            pass
                    else:
                        pass
            my_doc.save(doc_path)
            # print(final_list)
        openfile.close()




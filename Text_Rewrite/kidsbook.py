import bs4
import requests
from bs4 import BeautifulSoup as bs
from urllib import request
import re
import os
import urllib
import csv

# scrape and download


URL = 'https://www.gutenberg.org/files/'

with open('C:/Users/Andrew/Documents/kidsbookname.csv', 'r') as file:
    names = csv.reader(file)
    name_list = []
    for name in names:
        book_name = ''.join(name)
        name_list.append(book_name)
        print(book_name)

with open('C:/Users/Andrew/Documents/kidsbook.csv', 'r') as num:
    numbers = csv.reader(num)
    n = 0
    for number in numbers:
        book_number = ''.join(number)
        print(book_number)
        try:
            # url = "https://www.gutenberg.org/files/" + book_number + "/" + book_number + "-0.txt"
            url = "https://www.gutenberg.org/ebooks/" + book_number + ".txt.utf-8"
            # https://www.gutenberg.org/ebooks/19033.txt.utf-8
            print(url)
            fullfilename = os.path.join(r"D:\ScarlettBooks\temp", name_list[n])
            print(fullfilename)
            request.urlretrieve(url, fullfilename)
        except:
            print('error:' + name_list[n])
            pass
        n = n + 1


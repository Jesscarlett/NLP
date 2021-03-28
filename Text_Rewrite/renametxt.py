import bs4
import requests
from bs4 import BeautifulSoup as bs
from urllib import request
import re
import os
import urllib
import csv

#

path = 'D:\\ScarlettBooks\\temp\\temp'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    print(f)
    # os.rename(f, f"{f}.txt")

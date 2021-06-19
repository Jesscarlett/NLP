import json
from bs4 import BeautifulSoup as bs
from urllib import request
import urllib
import re

data1 = {}
with open("D:/ScarlettBooks/Children-Stories/primarywords.json") as file:
    word_dict = json.load(file)
for k in word_dict:
# for count, k in enumerate(word_dict):
    # if count > 100:
    #     break
    string = str(word_dict[k])
    if len(string) > 600:
        print(k)
        print(len(string))
        try:
            # html = _get_soup_object("http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(
            #     term))
            url = "http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(k)
            hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0)'}
            req = urllib.request.Request(url, headers=hdr)
            page_html = urllib.request.urlopen(req).read()
            page_soup = bs(page_html, "html.parser")
            types = page_soup.findAll("h3")
            length = len(types)
            lists = page_soup.findAll("ul")
            out = {}
            for a in types:
                reg = str(lists[types.index(a)])
                meanings = []
                for x in re.findall(r'\((.*?)\)', reg):
                    if 'often followed by' in x:
                        pass
                    elif len(x) > 5 or ' ' in str(x):
                        meanings.append(x)
                name = a.text
                out[name] = meanings
            # return out
            # print(out)
            m = str(out)
            word_mean = m.translate(str.maketrans({'{': None,
                                                      '}': None,
                                                      "[": None,
                                                      "]": None,
                                                      "'": None,
                                                      "'": None,
                                                      "(": None,
                                                      ")": None}))
            word_meaning = word_mean[0:470]
        except Exception as e:
            # print('meaning not found'.format(k))
            word_meaning = 'not found'
        try:
            url2 = "https://www.synonym.com/synonyms/{0}".format(k)
            hdr2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0)'}
            req2 = urllib.request.Request(url2, headers=hdr2)
            page_html2 = urllib.request.urlopen(req2).read()
            page_soup2 = bs(page_html2, "html.parser")
            section = page_soup2.find('div', {'class': 'type-synonym'})
            spans = section.findAll('a')
            synonyms =[]
            for i, span in enumerate(spans):
                synonyms.append(span.text.strip())
                i += 1
                if i > 3:
                    break
            # if formatted:
            #     return {term: synonyms}
            # print(synonyms)
            word_synonym = str(synonyms).translate(str.maketrans({'{': None,
                                                                  '}': None,
                                                                  "[": None,
                                                                  "]": None,
                                                                  "'": None,
                                                                  "'": None,
                                                                  "(": None,
                                                                  ")": None}))
        except:
            # print("{0} has no Synonyms in the API".format(k)
            word_synonym = 'N/A'
        meaning = 'Meanings: ' + word_meaning + '... | Synonyms: ' + word_synonym + '. '
        data1[k] = meaning
    else:
        pass
print(data1)
word_dict.update(data1)
with open('D:/ScarlettBooks/Children-Stories/primarywords1.json', 'w') as json_file:
    json.dump(word_dict, json_file, indent=4, sort_keys=True)
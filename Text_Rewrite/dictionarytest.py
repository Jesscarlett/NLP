from bs4 import BeautifulSoup as bs
from urllib import request
import urllib
import re
import json
from Text_Rewrite.primary_words import word_list


# dictionary = PyDictionary()
#
# meaning = dictionary.meaning('overflow')
# print(meaning)
# print(type(meaning))
# print(str(meaning[0]), str(meaning[1]))

# print(dictionary.printMeanings())
# print(dictionary.getMeanings())
# print(dictionary.getSynonyms())
# val_list = dictionary.getMeanings()
# print(str(val_list))
# for val in val_list:
#     print(val)
# print(type(val))
# parts = val.keys()
# print(parts)
# pos = []
# for part in parts:
#     pos.append(part)
# print(pos)


data = {}

for term in word_list:

    if len(term.split()) > 1:
        print("Error: A Term must be only a single word")
    else:
        try:
            # html = _get_soup_object("http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(
            #     term))
            url = "http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(term)
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
            word_meaning = m.translate(str.maketrans({'{': None,
                                                      '}': None,
                                                      "[": None,
                                                      "]": None,
                                                      "'": None,
                                                      "'": None,
                                                      "(": None,
                                                      ")": None}))

        except Exception as e:
            print('meaning not found'.format(term))
            word_meaning = 'not found'
            # if disable_errors == False:
            # print("Error: The Following Error occured: %s" % e)
        try:
            url2 = "https://www.synonym.com/synonyms/{0}".format(term)
            hdr2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0)'}
            req2 = urllib.request.Request(url2, headers=hdr2)
            page_html2 = urllib.request.urlopen(req2).read()
            page_soup2 = bs(page_html2, "html.parser")
            section = page_soup2.find('div', {'class': 'type-synonym'})
            spans = section.findAll('a')
            synonyms = [span.text.strip() for span in spans]
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
            print("{0} has no Synonyms in the API".format(term))
            word_synonym = 'N/A'

    meaning = 'Meanings: ' + word_meaning + '. | Synonyms: ' + word_synonym + '. '

    data[term] = meaning
    print(data)

with open('D:/ScarlettBooks/Children-Stories/primarywords.json', 'w') as json_file:
    json.dump(data, json_file, indent=4, sort_keys=True)

from bs4 import BeautifulSoup as bs
from urllib import request
import urllib
import re
import json
from PyDictionary import PyDictionary
from Text_Rewrite.primary_words import word_list
import random
import time

header1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/47.3'}
header2 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
header3 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4'}
header4 = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
header_list = [header1, header2, header3, header4]

with open('D:/ScarlettBooks/Children-Stories/sentencepos.json', 'r') as file:
    data = json.load(file)

# data = {}
terms = ['theater', 'theatre', 'their', 'them', 'theme', 'themselves', 'then', 'theology', 'theory', 'therapy', 'there', 'therefore', 'thermometer', 'thermosphere', 'these', 'they', 'thick', 'thickshake', 'thigh', 'thin', 'thing', 'think', 'thinking', 'third', 'thirteen', 'thirty', 'this', 'thongs', 'thorn', 'thorough', 'thoroughly', 'those', 'though', 'thought', 'thoughtfully', 'thousand', 'thousandth', 'thread', 'threat', 'threaten', 'threatening', 'three', 'thrifty', 'thrilling', 'thrive', 'throat', 'through', 'throughout', 'throw', 'thug', 'thumb', 'thumbnail', 'thump', 'thunder', 'thus', 'thwart', 'thyme', 'ticket', 'tickle', 'tie', 'tied', 'tiger', 'tight', 'tightly', 'timber', 'time', 'timid', 'tingle', 'tinsel', 'tiny', 'tip', 'tire', 'tired', 'tissue', 'titan', 'title', 'to', 'toaster', 'tobacco', 'tobacconist', 'today', 'toe', 'together', 'toilet', 'tolerable', 'tolerate', 'tolerating', 'tomato', 'tomb', 'tomorrow', 'tone', 'tongue', 'tonight', 'tonsil', 'tonsils', 'too', 'took', 'tool', 'tooth', 'top', 'topic', 'tornado', 'torrential', 'torso', 'tortoise', 'torture', 'toss', 'total', 'totally', 'touch', 'tough', 'tour', 'tourist', 'tournament', 'toward', 'towards', 'towel', 'tower', 'towering', 'town', 'toxic', 'toy', 'trace', 'track', 'tracksuit', 'trade', 'tradition', 'traditional', 'traffic', 'tragedy', 'trail', 'train', 'training', 'traitor', 'tranquil', 'transfer', 'transferred', 'transferring', 'transform', 'transformation', 'transition', 'translate', 'translation', 'transmit', 'transmitted', 'transportation', 'trap', 'trash', 'trauma', 'travel', 'traveled', 'traveling', 'travelled', 'traveller', 'travelling', 'trawler', 'treasure', 'treat', 'treatment', 'treaty', 'tree', 'tremendous', 'tremendously', 'tremor', 'trend', 'trendy', 'trial', 'tribal', 'tribe', 'trick', 'tricky', 'trilogy', 'trinity', 'trio', 'trip', 'triple', 'triumph', 'triumphantly', 'troop', 'trophy', 'tropical', 'troposphere', 'trouble', 'trounce', 'trousers', 'trout', 'truck', 'true', 'truly', 'truncheon', 'trust', 'trustworthy', 'truth', 'truthful', 'truthfully', 'try', 'trying', 'tube', 'tuesday', 'tumble', 'tundra', 'tunnel', 'turbulence', 'turn', 'turquoise', 'turtle', 'tv', 'twelfth', 'twelve', 'twenty', 'twice', 'twilight', 'twin', 'two', 'type', 'typhoon', 'typical', 'typically', 'tyranny', 'ugly', 'ultimate', 'ultimately', 'ultrasound', 'umbrella', 'umpire', 'unabashed', 'unable', 'unacceptable', 'unauthorized', 'unbeatable', 'unbeaten', 'unbelievable', 'uncensored', 'uncharted', 'uncle', 'unconditional', 'unconscious', 'unconventional', 'undefeated', 'under', 'undercover', 'undergo', 'underground', 'underhanded', 'underline', 'underneath', 'undernourished', 'underpants', 'understand', 'understanding', 'understood', 'underwear', 'undisclosed', 'undiscovered', 'unduly', 'unemployment', 'unenforceable', 'unexpected', 'unexplained', 'unexplored', 'unforgettable', 'unfortunately', 'unicycle', 'uniform', 'union', 'unique', 'unit', 'unite', 'united', 'universal', 'universe', 'university', 'unknown', 'unleash', 'unless', 'unlike', 'unlikely', 'unlock', 'unnecessary', 'unpredictable', 'unreachable', 'unsanitary', 'unspoken', 'unsung', 'untamed', 'until', 'untold', 'untouched', 'unusual', 'unveiled', 'up', 'uplifting', 'upon', 'upper', 'upsell', 'upsetting', 'uranus', 'urban', 'urge', 'us', 'use', 'used', 'useful', 'useless', 'user', 'usher', 'using', 'usual', 'usually', 'utensil', 'utility', 'utopia', 'vacant', 'vacantly', 'vacation', 'vaccinate', 'vacillate', 'vacuum', 'vaguely', 'vainly', 'valiant', 'valiantly', 'valley', 'valor', 'valuable', 'value', 'vanilla', 'vanish', 'vanquish', 'vaporize', 'variable', 'variation', 'variety', 'various', 'varnish', 'vary', 'vase', 'vast', 'vastly', 'vegetable', 'vehicle', 'vein', 'velvet', 'venom', 'venomous', 'venture', 'venus', 'verb', 'verbally', 'verdant', 'verdict', 'verify', 'version', 'versus', 'vertex', 'vertical', 'vertigo', 'very', 'vessel', 'vest', 'veteran', 'via', 'vibration', 'vicious', 'viciously', 'victim', 'victoriously', 'victory', 'video', 'vietnamese', 'view', 'viewer', 'vigilant', 'vigorously', 'vile', 'village', 'villain', 'violate', 'violation', 'violence', 'violent', 'violently', 'violet', 'violin', 'virginia', 'virtually', 'virtue', 'virtuoso', 'virus', 'visible', 'vision', 'visit', 'visitor', 'visual', 'visualize', 'vital', 'vitamin', 'vitamins', 'vivacious', 'vivaciously', 'vocabulary', 'vocal', 'vocalize', 'voice', 'volatile', 'volcano', 'volts', 'volume', 'voluntarily', 'volunteer', 'voluptuous', 'voracious', 'vote', 'voter', 'voucher', 'vowel', 'voyage', 'vs', 'vulgar', 'vulnerable', 'vulture', 'wacky', 'wage', 'wagon', 'waist', 'wait', 'wake', 'walk', 'wall', 'wallaby', 'walrus', 'wander', 'want', 'wanted', 'wanton', 'war', 'warm', 'warmly', 'warn', 'warning', 'warped', 'wash', 'washington', 'waste', 'watch', 'water', 'watercress', 'wave', 'way', 'we', 'weak', 'weakly', 'wealth', 'wealthy', 'weapon', 'wear', 'wearily', 'weary', 'weather', 'weave', 'webbed', 'wedding', 'wedge', 'wednesday', 'week', 'weekend', 'weekly', 'weigh', 'weight', 'weir', 'weird', 'welcome', 'welfare', 'well', 'went', 'were', 'west', 'western', 'wet', 'wetland', 'wetly', 'wharf', 'what', 'whatever', 'wheat', 'wheel', 'wheeze', 'when', 'whenever', 'where', 'whereas', 'whether', 'which', 'whiff', 'while', 'whimsical', 'whine', 'whinge', 'whinger', 'whip', 'whisper', 'whistle', 'white', 'whiting', 'who', 'whole', 'wholly', 'whom', 'whopping', 'whose', 'why', 'wide', 'widely', 'widespread', 'width', 'wife', 'wigwam', 'wild', 'wilderness', 'wildly', 'will', 'willfully', 'willing', 'willow', 'win', 'wind', 'window', 'wine', 'wing', 'winner', 'winning', 'winter', 'wipe', 'wire', 'wisconsin', 'wisdom', 'wise', 'wisely', 'wish', 'with', 'withdraw', 'withheld', 'withhold', 'within', 'without', 'witness', 'woefully', 'wolf', 'wolves', 'woman', 'wombat', 'women', 'wonder', 'wonderful', 'wonderfully', 'wondrous', 'wood', 'wooden', 'woodland', 'word', 'work', 'worker', 'working', 'works', 'workshop', 'world', 'worldwide', 'worn', 'worried', 'worriedly', 'worry', 'worst', 'worth', 'would', 'wouldn’t', 'wound', 'wounded', 'wrap', 'wrench', 'wrinkle', 'wrinkly', 'wrist', 'wristwatch', 'write', 'writer', 'writing', 'written', 'wrong', 'wrongly', 'wrote', 'xylophone', 'yacht', 'yams', 'yard', 'yawn', 'yawningly', 'yeah', 'year', 'yearly', 'yearning', 'yearningly', 'yeast', 'yell', 'yelled', 'yellow', 'yes', 'yesterday', 'yet', 'yield', 'yieldingly', 'yoghurt', 'you', 'young', 'your', 'yours', 'yourself', 'youth', 'youthfully', 'yummy', 'zany', 'zeal', 'zealously', 'zebra', 'zero', 'zest', 'zestfully', 'zestily', 'zone', 'zoology']
for term in terms:
    data[term] = {}
    try:
        url = "https://tangorin.com/sentences?search=" + term
        # hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0)'}
        hdr = random.choice(header_list)
        req = urllib.request.Request(url, headers=hdr)
        page_html = urllib.request.urlopen(req).read()
        page_soup = bs(page_html, "html.parser")
        my_divs = page_soup.find_all("dd", {"class": 's-en'})
        if not my_divs:
            print(term + ': not found')
            try:
                url = "https://sentencedict.com/" + term + '.html'
                # hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0)'}
                hdr = random.choice(header_list)
                req = urllib.request.Request(url, headers=hdr)
                page_html = urllib.request.urlopen(req).read()
                page_soup = bs(page_html, "html.parser")
                my_divs = page_soup.find_all("div", {"id": 'all'})
                for my_div in my_divs:
                    p_str = my_div.text.strip()
                    # print(p_str)
                    s = re.search('1.(.*?)2.', p_str).group(1)
                    print(s)
                    data[term]['sentence'] = s
                    break
            except:
                pass
        else:
            for my_div in my_divs:
                p_str = my_div.text.strip()
                print(p_str)
                data[term]['sentence'] = p_str
                break
    except:
        pass
    try:
        dictionary = PyDictionary(term)
        val_list = dictionary.getMeanings().values()
        for val in val_list:
            print(val)
            print(type(val))
            parts = val.keys()
        new_pos = list(set(parts))
        print(new_pos)
        data[term]['pos'] = str(new_pos)
    except:
        pass
    with open('D:/ScarlettBooks/Children-Stories/sentencepos1.json', 'w') as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)
    time.sleep(3)


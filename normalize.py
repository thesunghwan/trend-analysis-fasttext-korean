import re
import sys

#from konlpy.tag import Kkma
#from konlpy.utils import pprint
#kkma = Kkma()

from konlpy.tag import Twitter
twitter = Twitter()


#filename = "raw_articles.txt"

raw_file = open('data/' + sys.argv[1])
train_file = open('data/normalized_' + sys.argv[1], 'w')

text = ""

for lines in raw_file:
    parenthesis_removed = re.sub(r'\([^)]*\)', '', lines)
    alphanumeric = re.sub(r'[^\w]', ' ', parenthesis_removed)
    #final = re.sub(r'으로\b|로서\b|되어\b|만큼\b|부터\b|에서\b|에겐\b|이야말\b|이다\b|에게만\b|[은나에의가와는를로를과은을이과와도인에식씨뿐만인]\b', '', alphanumeric);
    final = twitter.nouns(alphanumeric)
    final = ' '.join(final)

    text = text + final

train_file.write(text)    

raw_file.close()
train_file.close()

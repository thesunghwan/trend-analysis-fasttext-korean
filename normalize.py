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
    final = re.sub(r'으로\b|로서\b|되어\b|만큼\b|부터\b|에서\b|에겐\b|이야말\b|이다\b|에게만\b|에게\b|처럼\b|당장나\b|에게서\b|정권\b|이명박근혜\b|대통령\b|박근헤\b|내려와라_박근혜\b|a이게나라랴\b|청와대발\b|하여라\b|박근혜와\b|박근혜정권퇴진\b|이게나라랴\b|박근혜정권퇴진\b|바로가기박근혜\b|박근혜와\b|박근혜퇴진\b|박근혜대통령\b|국정논단\b|하야반대\b|[표씨으은나에의가와는를로를과은을이과와도인에식씨뿐만인할]\b', '', alphanumeric);
    #final = twitter.nouns(alphanumeric)
    #final = ' '.join(final)

    text = text + final

train_file.write(text)

raw_file.close()
train_file.close()

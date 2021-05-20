from nltk.corpus import words

from nltk import FreqDist
from nltk.corpus import brown
import pprint

frequency_list = FreqDist(i.lower() for i in brown.words())
most_common = frequency_list.most_common()
# print(len(brown.words())) # 1161192 total words
# print(len(most_common)) # 49815 unique words.
top_ten = []

for i in most_common:
    if len(top_ten) < 10000:
        word = i[0]
        if word.isalpha() and len(word) > 4:
            top_ten.append(word)

fileObj = open('top_ten_5_or_longer.py', 'w')
fileObj.write('top_ten = ' + pprint.pformat(top_ten) + '\n')

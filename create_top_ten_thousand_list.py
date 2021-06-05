from nltk.corpus import words

from nltk import FreqDist
from nltk.corpus import brown
import pprint

frequency_list = FreqDist(i.lower() for i in brown.words())
most_common = frequency_list.most_common()
# print(len(brown.words())) # 1161192 total words
# print(len(most_common)) # 49815 unique words.
# print(most_common[:20])


for i in range(7):
    top_ten = []
    for word_index in range(10000):
        word = most_common[word_index][0]
        if word.isalpha() and len(word) > i:
            top_ten.append(word)

    fileObj = open(f'top_ten_{i + 1}_or_longer.py', 'w')
    fileObj.write('top_ten = ' + pprint.pformat(top_ten) + '\n')

# Type-Fastly
Exploring the potential for using a custom Input Method Editor for typing faster

## Introduction

A while ago I had an idea: What if I could type using only the middle row on a keyboard? In theory, I could type faster without having to ever move my fingers off of home row, and my computer should be able to interpret what words I'm trying to spell based only on the finger being used for that keystroke. I coded up a simple program that would try to guess what word I was intending to spell based on this strategy. Pretty quickly I discovered numerous words which would be spelled the same way using only home row letters. Rather than immediately recognizing that this was a bad idea, I decided to pursue a method of quantifying *how* bad of an idea this is. 

In this project I created a program which calculates what percentage of common words could not be fully defined based on home row letters alone. I also explore how increasing the length of words affects feasibility. 

I'm using the Dvorak keyboard layout, which already favors the middle row a lot when typing. Here's what the layout looks like:

    '  ,  .  p  y  f  g  c  r  l
    a  o  e  u  i  d  h  t  n  s
    ;  q  j  k  x  b  m  w  v  z

## Terminology 

Homerownly - a portmanteau of 'home row', and 'only'. I use this to describe the spelling of words using only letters on the middle row of a keyboard
Homronyms - some homerownly spellings are the same for multiple words. I call these words 'homronyms'. 

## How it Works

First, I use `create_top_ten_thousand_list.py` to create 7 lists words of length at least 1 to 7, respectively. These lists are pulled from the top 10000 words, so the lengths of the lists decrease as the minimum word length increases. This will let me compare the feasibility of this typing method by excluding shorter words. This program uses the Brown Corpus to calculate the most frequently used words. 

Then, with `feasibility_test.py`, each of these words are converted to their homerownly spellings. These spellings are compared to see if multiple words share the same homerownly spelling. 

I ran the feasibility test with each list of the top ten-thousand words. My prediction is that feasibility will increase drastically as the short words are removed. 

## Results


 | Minimum Word Length  | Number of Duplicates  |  Total Words | Percentage Unique  |
| ------------ | ------------ | ------------ | ------------ |
| 1  |423| 9519 | 95.56%   |
| 2 | 415 | 9497 | 95.63% |
| 3 | 406 | 9442 | 95.70% |
| 4 | 347 | 9144 | 96.21% |
| 5 | 197 | 8189 | 97.59% |
| 6 | 99 | 6899 | 98.57% | 
| 7 | 42 | 5366 | 99.22% |

Ideally this method of typing would work with all lengths of words, but even excluding short words, there are still enough to make this method annoying, and counterintuitive. 

Some examples of homronyms I found are:

    kitchen, pitcher
    still, swiss
    frighten, brighter
    those, whole, whose, chose
    store, score, stone, stove, swore
    rationality, nationality
    changing, charming, charging

If some of these were entirely obscure words, it wouldn't be a problem for most use cases, but the commonality present here makes this method pretty useless if it gets 3 words wrong out of 100.

I tried the same code with a QWERTY layout and achieved an increase in about 0.5% of unique homrownly spellings across each list of words. 

## Future Development 

It would be possible to create an IME scheme with this strategy which could provide seamless integration into an operating system. Perhaps with NLP it could be made reasonably reliable. 

My next planned improvement is testing whether feasibility increases to reasonable levels by using 2 of 3 rows on the keyboard, although the benefit/cost ratio is pretty low at that point. 

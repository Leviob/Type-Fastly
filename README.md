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

First, I use `create_top_ten_thousand_list.py` to create 7 lists of the top ten-thousand words of length at least 1 to 7, respectively. This will let me compare the feasibillity of this typing method by excluding shorter words. This program uses the Brown Corpus to calculate the most frequently used words. 

Then, with `feasibillity_test.py`, each of these words are converted to their homerownly spellings. These spellings become the keys of a dictionary, with the values being the word or words the spelling can represent. 

I ran the feasibillity test with each list of the top ten-thousand words. My prediction is that feasibility will increase drastically as the short words are removed. 

## Results

## Future Development 

It would be possible to create an IME scheme with this strategy which could provide seamless integration into an operating system. 

My next planned improvement is testing whether feasibility increases to reasonable levels by using 2 of 3 rows on the keyboard, although the benefit/cost ratio is pretty low at that point. 

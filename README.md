# Type-Fastly
Exploring the potential for using a custom Input Method Editor for typing faster

## Introduction

A while ago I had an idea: What if I could type using only the middle row on a keyboard? In theory, I could type faster without having to ever move my fingers off of home row, and my computer should be able to interpret what words I'm trying to spell based only on the finger being used for that keystroke. I coded up a simple program that would try to guess what word I was intending to spell based on this strategy. Pretty quickly I discovered numerous words which would be spelled the same way using only home row letters. Rather than immediately recognizing that this was a bad idea, I decided to pursue a method of quantifying *how* bad of an idea this is. 

In this project I created a program which calculates what percentage of common words could not be fully defined based on home row letters alone. I also explore how increasing the length of words affects feasibility. 

## Terminology 

Homerownly - a portmanteau of 'home row', and 'only'. I use this to describe the spelling of words using only letters on the middle row of a keyboard
Homronyms - some homerownly spellings are the same for multiple words. I call these words 'homronyms'. 

## How it Works

# for word in top_ten(thousand)
# find the homerownly spelling
# add that value to a dictionary 
#   key is the homerownly spelling
#   value is a list of words with that spelling (homronyms)

## Future Development 

It would be possible to create an IME scheme with this strategy which could provide seamless integration into an operating system. 

My next planned improvement is testing whether feasibility increases to reasonable levels by using 2 of 3 rows on the keyboard, although the benefit/cost ratio is pretty low at that point. 

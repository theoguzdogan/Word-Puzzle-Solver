import os
import re
import readline
from typing import Counter

max_letter_amount = 8
word_construction = str(input("Sample: **a*\nEnter the word: "))
letter_amount = len(word_construction)
given_letters = str(input("Sample: abcdefgh\nEnter the letters: "))
list = []

for letter in given_letters:
    
    file = open("database/{0}.txt".format(letter.upper()))
    while True:
        word = file.readline()
        is_to_take = 1
        if not word:
            break
        for search_letter in word:
            if search_letter not in given_letters:
                is_to_take = 0
                
                
        if is_to_take == 1:
            list.append(word)
    file.close()

print(list)
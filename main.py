from doctest import master
import os
import re
import readline
from typing import Counter

max_letter_amount = 8
word_construction = str(input("Sample: **a*\nEnter the word: "))
letter_amount = len(word_construction)
given_letters = list(input("Sample: abcdefgh\nEnter the letters: "))
wordlist = []
word_specialties = {}
counter = 0
for item in word_construction:
    if item == "*":
        counter+=1
        continue
    else:
        word_specialties[counter] = item
        counter+=1
#print(word_specialties)

checked_letters = []
for letter in given_letters:
    if letter in checked_letters:
        continue
    else:
        checked_letters.append(letter)

    file = open("database/{0}.txt".format(letter.upper()))

    while True:
        word = file.readline()
        if not word:
            break
        if (len(word)-1)==letter_amount:
            is_compatible = True
            for i in word_specialties.keys():
                if word[i]!=word_specialties[i]:
                    is_compatible = False
            if is_compatible:
                wordlist.append(word)
    file.close()
for i in range(len(wordlist)):
    wordlist[i] = wordlist[i][0:-1]

#print(wordlist)
final_list = []
for word in wordlist:
    is_conserved = True
    letters_copy = given_letters.copy()
    for letter in word:
        if letter in letters_copy:
            letters_copy.remove(letter)
        else:
            is_conserved = False
    if is_conserved:
        final_list.append(word)

print("Possibilities:")
for i in range(len(final_list)):
    print("%d> %s" % ((i+1), final_list[i]))
print("---------------")
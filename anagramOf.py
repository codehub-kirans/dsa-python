##################################################################
##
##                       DOCUMENTATION
##
##################################################################
#
#
# @file	anagramOf.py
# @version	1
# @author	Kiran S
# @short	AnagramFinder
# Implementation of Anagram Finder using recursion and loops
#
# <p>
# See GIT for detailed history.
# <p>
# Copyright (c) 2021 Kiran S. All rights reserved.
#
##################################################################
def anagramOf(string):
    if len(string) <= 1:
        return string[0:]
    anagramList = anagramOf(string[1:])

    collections = []
    for anagram in anagramList:
        for index in range(0, len(anagram) + 1):
            newAnagram = list(anagram)
            newAnagram.insert(index, string[0])
            collections.append("".join(newAnagram))
    
    #print("Collection Growth: ", collections)
    #print()
    return collections

#Test Anagrams
print(anagramOf('abcde'))
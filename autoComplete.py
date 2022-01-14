##################################################################
##
##                       DOCUMENTATION
##
##################################################################
#
#
# @file	autoComplete.py
# @version	1
# @author	Kiran S
# @short	Word Autocomplete & autocorrect
# Autocomplete using Tries
#
# <p>
# See GIT for detailed history.
# <p>
# Copyright (c) 2022 Kiran S. All rights reserved.
#
##################################################################


class TrieNode:
    def __init__(self) -> None:
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root

        for char in word:
            childNode = currentNode.children.get(char)
            if childNode is not None:
                currentNode = childNode
            else:
                return None

        return currentNode

    def longestMatch(self, word):
        currentNode = self.root
        longestMatch = ""

        for char in word:
            childNode = currentNode.children.get(char)
            if childNode:
                currentNode = childNode
                longestMatch += char
            else:
                break

        return longestMatch, currentNode

    def keyTraversal(self, node=None, keyString=[]):
        currentNode = node or self.root
        keys = ""
        if currentNode:
            for childkey, childnode in currentNode.children.items():
                keys = keys + childkey + ","
            keyString.append(keys[:-1])

            for childkey, childnode in currentNode.children.items():
                if childkey != "*":
                    self.keyTraversal(childnode, keyString)
        return keyString

    def insert(self, word):
        currentNode = self.root

        for char in word:
            childNode = currentNode.children.get(char)

            if childNode is not None:
                currentNode = childNode
            else:
                childNode = TrieNode()
                currentNode.children[char] = childNode
                currentNode = childNode

        currentNode.children["*"] = None

    def collectWords(self, node=None, word="", words=[]):
        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectWords(childNode, word + key, words)

        return words

    def autoCompleteWord(self, prefix):
        searchNode = self.search(prefix)
        if searchNode:
            return self.collectWords(searchNode)
        else:
            return None

    def autoCorrectWord(self, prefix):
        searchNode = self.search(prefix)
        words = []

        if searchNode:
            return prefix
        else:
            longestMatch, startNode = self.longestMatch(prefix)
            self.collectWords(startNode, longestMatch, words)

        return words


# Test
autoComplete = Trie()
autoComplete.insert("cat")
autoComplete.insert("man")
autoComplete.insert("maul")
autoComplete.insert("can")
autoComplete.insert("call")
print("Autocomplete for ca: ", autoComplete.autoCompleteWord("ca"))
print("Autocomplete for ma: ", autoComplete.autoCompleteWord("ma"))
print("Autocomplete for z: ", autoComplete.autoCompleteWord("z"))
print("Keys: ", autoComplete.keyTraversal())
print("Autocorrect for mat: ", autoComplete.autoCorrectWord("mat"))
print("Autocorrect for cad: ", autoComplete.autoCorrectWord("cad"))

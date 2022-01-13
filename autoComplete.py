"""Autocomplete using Tries"""

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

        currentNode.children['*'] = None

    def collectWords(self, node = None, word = "", words = []):
        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            if key == "*":
                words = words.append(word)
            else:
                self.collectWords(childNode, word+key, words)
        
        return words

    def autoCompleteWord(self, prefix):
        searchNode = self.search(prefix)
        if searchNode:
            return self.collectWords(searchNode, prefix, [])
        else:
            return None

#Test
autoComplete = Trie()
autoComplete.insert("cat")
autoComplete.insert("man")
autoComplete.insert("maul")
autoComplete.insert("can")
autoComplete.insert("call")
print("Autocomplete for ca: ", autoComplete.autoCompleteWord("ca"))
print("Autocomplete for ma: ", autoComplete.autoCompleteWord("ma"))
print("Autocomplete for z: ",autoComplete.autoCompleteWord("z"))
        
        


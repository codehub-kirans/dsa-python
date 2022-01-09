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
    
    return collections

#Test Anagrams
print(anagramOf('abcde'))
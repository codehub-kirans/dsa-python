def findMissingLetter(string):
    stringHashTable = {}
    for character in string:
        stringHashTable[character] = True

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    isMissingAlphabet = False

    for letter in alphabet:
        if stringHashTable.get(letter) is None:
            print("Missing Alphabet is ", letter)
            isMissingAlphabet = True
            break
    if not isMissingAlphabet:
         print("No missing Alphabets")

findMissingLetter("the quick brown box jumps over a lazy dog")
"""
Generate all the reorderings of a set of letters.
Get this code reviewed...
"""

def word_ordering(word):
    if len(word)==1:
        return [word]
    newWords = []
    for i in range(len(word)):
        char = word[i]
        newlist = word[0:i]+word[i+1:]
        list = word_ordering(newlist)
        for i in range(len(list)):
            list[i] = char + list[i]
        newWords.extend(list)
    return  newWords

print word_ordering('abc')

#Tail


# This needs to be optimize
def scrabbleWords(tiles):
    if len(tiles)==1:
        return [tiles]
    newWords = []
    for i in range(len(tiles)):
        tile = tiles[i]
        leftOver = tiles[0:i] +  tiles[i+1:]
        words = scrabbleWords(leftOver)
        print words
        for word in words:
            newWord = tile + word
            if word not in newWords:
                newWords.append(word)
            newWords.append(newWord)
    return newWords

print scrabbleWords('abc')
import string
''' This program takes a text file and gives the total
length of the character in the file along with the frequency
of each alphabet and as well as most and least common 10 alphabets'''

"""Character frequency"""

'''Total number of characters'''

def character_analysis(filename):
    hist = {}
    file = open(filename)   # process file object
    listOfWords = []  # converts the file to the list
    for i in file:
        someword = i.strip()   # removes the whitespace and extra lines
        listOfWords.append(someword)
    wordDict = {}
    for word in listOfWords:
        for letter in word:
            if letter in wordDict:  # checks to see if the letter is already in the dictionary
                wordDict[letter] += 1   # add one if does otherwise create a new key and value
            else:
                wordDict[letter] = 1
    return wordDict

def sumOfCharacters(aDict):
    sum = 0
    for i in aDict.values(): #sums all the values in the dictionary
        sum = sum + i
    return sum

def most_common(aDict):
    t = []
    for key, value in aDict.items():
        t.append((value, key))
    t.sort(reverse=True)
    g = []
    for i, value in enumerate(t):
        g.append((t[i][1], t[i][0]))   # to swap the value tuples
    return g[:10]

def least_common(aDict):
    t = []
    for key, value in aDict.items():
        t.append((value, key))
    t.sort()
    g = []
    for i, value in enumerate(t):
        g.append((t[i][1], t[i][0]))
    return g[:10]

allCharacters = character_analysis('words.txt')
print('All Characters in the words.txt: ', allCharacters)
print('Sum of all characters in the text:', sumOfCharacters(allCharacters))
print('The ten most common characters: ', most_common(allCharacters))
print('The ten least common characters: ', least_common(allCharacters))

nameOfFile = 'words.txt'
file = open(nameOfFile, 'r')

# Number of words in the List
def numOfWords():
    i = 0
    for i, word in enumerate(file):
        i += 1
    print('Number of words in the list:',i)
numOfWords()

# Average word length
file = open(nameOfFile)
def avgWord():
    sumOfLen = 0
    for i, word in enumerate(file):
        sumOfLen = sumOfLen + len(word.strip())
        i += 1
    average = sumOfLen// i # converted to integer
    return average
print('Average word length is:', avgWord())

# Maximum word length
file = open(nameOfFile)

def maxWord():
    maxWord = 0
    for i in file:
        word = i.strip()
        if (len(word) > maxWord):
            maxWord = len(word)
    return maxWord
print('Maxium word length is: ', maxWord())

# Number of words that use all vowels
file = open(nameOfFile)

def allVowels():
    count = 0
    vowels = 'aeiou'
    for i in file:
        allVowelsFound = True
        word = i.strip()
        for letter in vowels:
            if (letter not in word):
                allVowelsFound = False
        if (allVowelsFound):
            count+=1
    return count
print('Number of words that use all vowels: ', allVowels())

file = open(nameOfFile)

def abc():
    numOfAbc = 0
    for i in file:
        word = i.strip()
        abc = True
        previous = word[0]
        for i in word:
            if (i < previous):
                abc = False
            previous = i
        if(abc):
            numOfAbc += 1
    return numOfAbc
print('Number of abecedarian words: ', abc())

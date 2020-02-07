from collections import Counter

file = open('words.txt')
wordList = file.readlines()

def avoids():
    counter = Counter()
    counterCommon = []
    for i in wordList:
        for letters in set(i):
            counter[letters]+=1
            counterCommon = counter.most_common()
    forbiddenWord = counterCommon[21:]
    print(forbiddenWord)
    return forbiddenWord
avoids()

file = open('words.txt')
def combinations():
    count = 0
    forbiddenWord = 'wzxjq'
    for i in file:
        allForbiddenFound = False
        word = i.strip()
        for letter in word:
            if (letter in forbiddenWord):
                allForbiddenFound = True
        if (allForbiddenFound):
            count+=1
    return count
print('The 5 Forbidden letters that excludes the smallest number of words is :', combinations())

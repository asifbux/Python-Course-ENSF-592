# Open the text document that you want to Analyze by
# entering the name below

nameOfFile = 'chapter1.1.txt'
file = open(nameOfFile)

def numOfWords():
    counter = 0
    for words in file:
        word = words.split()
        counter += len(word)
    return counter
print('Number of Words in text is :', numOfWords())

file = open(nameOfFile)
txt = file.readlines() # one array list

def numOfSentences():
    sentenceCount = str(txt).split(".")
    return len(sentenceCount)

print('Average number of Sentences :', numOfSentences())
file = open(nameOfFile)

def avgWords():
    average = numOfWords()// numOfSentences()
    return average

print('Average number of words per sentence is:', avgWords())

def avgNumOfSentence():
    counter = 0
    sentenceCount = str(txt).split('.')
    for i in str(sentenceCount).split(','):
        counter += 1
    average = counter// numOfSentences()
    return average
print('Average number of sentence parts is: ', avgNumOfSentence())

def numOfPersonalPronouns():
    counter = 0
    pronouns = [ "me", "he", "him", "my", "you", "we", "her", "us", "them", "I", "she", "they"]
    for i in str(txt).split():
        if i.lower() in pronouns:
            counter += 1
    return counter

print("Number of personal pronouns is: ", numOfPersonalPronouns())

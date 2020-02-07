import string
from scipy import stats

# Step 1: Get dictionary of words and frequency while cleaning
# the file. Get list of words with their frequency
def process_file(filename, skip_header):
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('FINIS'):
            break
        process_line(line, hist)

    return hist


def skip_gutenberg_header(fp):
    for line in fp:
        if line.startswith('CHAPTER I'):
            break


def process_line(line, hist):

    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1

allWords = process_file('emma.txt', True)


# Step 2: Get dict of word: word Length then put that in a list

def lenOfWords(dict):
    histLength = {}
    for keys in dict.keys():
        histLength[keys] = len(keys)
    return histLength

wordLength = lenOfWords(allWords)


def lenOfWordsList(dict):
    wordLengthList = []
    for i in dict:
        wordLengthList.append(dict[i])
    newList = wordLengthList[:100]
    return newList

lengthList = lenOfWordsList(wordLength)

#Step 3:Get a dict of all words with frequency form step 1 and put them in the list


def freqList(dict):
    frequencyList = []
    for i in dict:
        frequencyList.append(dict[i])
    newList = frequencyList[:100]
    newList.sort()
    newList.reverse()
    return newList

freqList = freqList(allWords)

#Step 4: Now we have all the necessary data to begin our Spearman analysis

def spearman(freqList, lengthList):

    # determine the length of the freq and length list which should be the same
    rangeOfFreq = range(len(freqList))
    rangeOfLength = range(len(lengthList))

    # This step will zip the ranks of frequency and wordLength together together

    sortedFreq = sorted(list(zip(freqList, rangeOfFreq)))
    sortedlength = sorted(list(zip(lengthList, rangeOfLength)))

    # Create temporary list of 0s

    rank1 = [0] * len(freqList)
    rank2 = [0] * len(lengthList)

    # for first iteration rank = 0 and value_index = (3, 3)

    for rank, value_index in enumerate(sortedFreq):
        rank1[value_index[1]] = rank + 1
    print("Rank of Frequency: ", rank1)

    # for first iteration rank = 0 and value_index = (3, 3)

    for rank, value_index in enumerate(sortedlength):
        rank2[value_index[1]] = rank + 1
    print("Rank of Word Length: ", rank2)

    diff = [x1 - x2 for (x1, x2) in zip(rank1, rank2)]
    print("Difference di: ", diff)

    diffSquared = []
    for i in diff:
        diffSquared.append(i ** 2)

    sumSpearman = 0

    for i in diffSquared:
        sumSpearman += i

    print("Sum of differences: ", sumSpearman)

    coefficient = 1 - ((6 * sumSpearman)/(100*(100*100 - 1)))

    print("Spearman's Coefficient from my algorithm: ", coefficient)

    spearman_rho, p = stats.spearmanr(freqList, lengthList)
    print("Scipy's Spearman Coefficient", spearman_rho)


print(spearman(freqList, lengthList))


def stats(dict1, dict2):
    listStat = []
    for keys in dict1.keys():
        if keys in dict2:
            listStat.append((dict1[keys], keys, dict2[keys]))
    listStat.sort()
    listStat.reverse()
    listStat = listStat[:30]
    return listStat

listStat = stats(allWords, wordLength)

def most_common(aDict):
    t = []
    for key, value in aDict.items():
        t.append((value, key))
    t.sort(reverse=True)
    g = []
    for i, value in enumerate(t):
        g.append((t[i][1], t[i][0]))
    return g[:10]

# Most common 30 Words and their frequency

print('The frequency and word length sorted by frequency: \n', stats(allWords, wordLength))
print('The frequent words are as following (shown only 30 words): \n', most_common(allWords))
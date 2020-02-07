 ASIF BUX

import string

"""Character frequency"""

'''Total number of characters'''


def process_file(filename):
    hist = {}
    file = open(filename)
    word = file.readlines()
    print(type(word))
    # for i in file:
    #     wordList = []
    #     wordList.append(i.strip())
    return wordList

    # for word in file:
    #     # putting all the characters
    #     for i in file:
    #
    #     # update the histogram
    #     hist[word] = hist.get(word, 0) + 1
    # return hist

allCharacters = process_file('words.txt')
print(allCharacters)
#
# '''The ten most common characters'''
#
#
# def most_common(hist):
#     t = []
#     for key, value in hist.items():
#         t.append((value, key))
#     t.sort()
#     t.reverse()
#     for freq, word in t[:10]:
#         print(word, ':', freq)
#     return t
#
#
# print(most_common(allCharacters))
#
# '''The ten least common characters'''
#
#
# def least_common(hist):
#     t = []
#     for key, value in hist.items():
#         t.append((value, key))
#     t.sort()
#     for freq, word in t[:10]:
#         print(word, ':', freq)
#     return t
#
#
# print(least_common(allCharacters))
import random

class Histogram(dict):
    """A histogram to count frequencies of elements.

    Inherits dict which will hold element-frequency pairs
    Elements are provided by Lists (iterables)
    """

    def __init__(self, l=None):
        """Constructor: provide elements in a list or iterable"""
        if l != None:
            self.count(l)

    def __str__(self):
        """ returns a string representation of each element-frequency pair"""
        # TODO: Add your code
        # For each entry in histogram, this should append to return string:
        # {value} count of {element}\n
        line = ''
        for key, value in self.items():
            line = line + '(' + str(value) + ' count of ' + str(key) + ')'
        for i in line:
            line = line.replace(')(', ')\n(')
        return line


    def __sub__(self, other):
        """Subtraction: Returns a dictionary with all keys that appear in self but not other.

        other: Histogram() object
        """
        # TODO: Add your code
        subDict = {}
        for key in self:
            if key not in other:
                subDict[key] = None
        return subDict

    def most_common(self, n=None):
        """Returns n most common (most frequent) elements in histogram

        if n=None, all are returned

        returns: List of Tuples, each Tuple is a element-frequancy pair
        """
        # TODO: Add your code
        # Follow analyze_book1 but make sure you add (element, frequency)
        t = []
        for key, value in self.items():
            t.append((value, key))
        t.sort(reverse=True)
        g = []
        for i, value in enumerate(t):
            g.append((t[i][1], t[i][0]))   # to swap the value tuples
        return g[:n]

    def count(self, l):
        """Adds items in list l to the histogram"""
        # TODO: Add your code
        for word in l:
            if word in self:
                self[word] += 1
            else:
                self[word] = 1
        return self

    def total_elements(self):
        """Returns the total of the frequencies in a histogram."""
        # TODO: Add your code
        sum = 0
        for i in self.values():
            sum += i
        return sum

    def different_elements(self):
        """Returns the number of different words in a histogram."""
        # TODO: Add your code
        sum = len(self)
        # for index, key in self.keys():
        #     sum += index
        return sum

    def random_element(self):
        """Chooses a random word from a histogram.

        The probability of each word is proportional to its frequency.
        returns: string a single words
        """
        # TODO: Add your code
        t = []
        for word, freq in self.items():
            t.extend([word] * freq)
        return random.choice(t)


def test(title, produced, expected):
    print("*** Test {}".format(title))
    if produced == expected:
        print("   PASS")
    else:
        print("   FAIL")
        print("   expected {}".format(expected))
        print("   produced {}".format(produced))

if __name__ == '__main__':

    a = [1, 2, 3, 1, 1, 2]
    b = 'Hello Calgary! What a great day. Calgary is a great city.'
    c = b.split()


    hist_int = Histogram()
    hist_int.count(a)

    hist_char = Histogram(b)

    hist_word = Histogram(c)

    test("Initialize with count()",
        str(hist_int),
        "(3 count of 1)\n(2 count of 2)\n(1 count of 3)")

    test("int hist most_common all",
        str(hist_int.most_common()),
        "[(1, 3), (2, 2), (3, 1)]")

    test("char hist most_common n=3",
        str(hist_char.most_common(n=3)),
        "[('a', 10), (' ', 10), ('y', 4)]")

    test("word hist most_common n=5",
        str(hist_word.most_common(n=5)),
        "[('great', 2), ('a', 2), ('is', 1), ('day.', 1), ('city.', 1)]")

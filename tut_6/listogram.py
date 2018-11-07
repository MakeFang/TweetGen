#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import math


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        target_index = self._index(word)
        if target_index is not None:
            self[target_index] = (word, self[target_index][1]+count)
            self.tokens += count
        else:
            self.append((word, count))
            self.tokens += count
            self.types += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        target_index = self._index(word)
        # print(target_index)
        return self[target_index][1] if target_index is not None else 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        return True if self._index(word) is not None else False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        for hist_index, hist_word in enumerate(self):
            if target == hist_word[0]:
                return hist_index
        else:
            return None


class SortedListogram(Listogram):

    def __init__(self, word_list=None):
        super(SortedListogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if word_list is not None:
            word_list.sort()
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        if len(self) == 0 or word > self[-1][0]:
            self.append((word, count))
            self.tokens += count
            self.types += 1
        elif word == self[-1][0]:
            self[-1] = (word, self[-1][1]+count)
            self.tokens += count
        else:
            target_index = self._cielindex(word)
            if self[target_index][0] == word:
                self[target_index] = (word, self[target_index][1]+count)
                self.tokens += count
            else:
                self.insert(target_index, (word, count))
                self.tokens += count
                self.types += 1

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        ciel_index = self._cielindex(target)
        if ciel_index >= len(self):
            return None
        return ciel_index if self[ciel_index][0] == target else None

    def _cielindex(self, target):
        if len(self) == 0:
            return None
        left = 0
        right = len(self)-1
        while left < right:
            middle = math.floor((left + right)/2)
            if self[middle][0] == target:
                return middle
            elif self[middle][0] < target:
                left = middle+1
            elif self[middle][0] > target:
                right = middle-1
        return left if self[left][0] >= target else left+1


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()

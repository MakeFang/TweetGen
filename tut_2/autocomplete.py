"""This script autocompletes words given starting characters.

This script uses list and iterate through the entire list for words that
satisfies the regex pattern. It currently runs .1 sec on my mac.
"""

import sys
import re
# import timeit


def read_dict():
    """Read the words from the default dictionary in OS X."""
    f = open('/usr/share/dict/words', 'r')
    word_list = f.read().replace('\n', ' ').split()
    # word_list = f.readlines()
    # word_list = [i for i in f]
    # for i in f:
    #     word_list.append(i.replace('\n', ''))
    f.close()
    return word_list


def autocomplete(word_start):
    """Autocomplete the input word.

    word_start: the beginning of the words needed to autocomplete.
    returns: a list of words that start with the input string.
    """
    word_list = read_dict()
    regex_pattern = '^' + word_start
    r = re.compile(regex_pattern)
    matched_words = filter(r.match, word_list)
    return list(matched_words)


if __name__ == '__main__':
    setup = '''
import random
import sys
from __main__ import autocomplete
'''
    # print(timeit.timeit("autocomplete(sys.argv[1])",
    #       setup=setup, number=100)/100)
    print(autocomplete(sys.argv[1]))

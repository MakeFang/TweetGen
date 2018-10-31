"""This script generate random words from macOS dictionary.

This version uses the default option open(). On my mac it takes around .04
seconds to run.
"""

import random
import sys
# import timeit


def read_dict():
    """Read the words from the default dictionary in OS X."""
    # f = open('/usr/share/dict/words', 'r')
    # word_list = f.read().replace('\n', ' ').split()
    # word_list = f.readlines()
    # word_list = [i for i in f]
    # for i in f:
    #     word_list.append(i.replace('\n', ''))
    # f.close()
    with open('/usr/share/dict/words', 'r') as f:
        word_list = f.read().replace('\n', ' ').split()
    return word_list


def rand_dict(word_length):
    """Generate random words from dictionary of given length.

    word_length: The amount of random words to return.
    returns a list of random words.
    """
    word_list = read_dict()
    random_words = random.sample(word_list, word_length)
    return random_words


if __name__ == '__main__':
    setup = '''
import random
import sys
from __main__ import rand_dict
'''
    # print(timeit.timeit("rand_dict(int(sys.argv[1]))",
    #       setup=setup, number=1000)/1000)
    argument = int(sys.argv[1])
    print(rand_dict(argument))

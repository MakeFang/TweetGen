"""This script autocompletes words given starting characters.

This script uses list and iterate through the entire list for words that
satisfies the regex pattern. It currently runs .1 sec on my mac.
"""

import sys
import re
# import timeit


def autocomplete(word_start):
    f = open('/usr/share/dict/words')
    word_list = [i for i in f]
    # for i in f:
    #     word_list.append(i)
    f.close()
    regex_pattern = '^' + word_start
    r = re.compile(regex_pattern)
    return list(filter(r.match, word_list))


if __name__ == '__main__':
    setup = '''
import random
import sys
from __main__ import autocomplete
'''
    # print(timeit.timeit("autocomplete(sys.argv[1])",
    #       setup=setup, number=100)/100)
    print(autocomplete(sys.argv[1]))

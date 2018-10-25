"""This script generate random words from macOS dictionary.

This version uses linecache, as suggested on stackexchange. It apparantely is
not suitable for big big file as it load the whole file into memory. On my mac
it takes around 2e-5 seconds to run.
"""

import random
import sys
import timeit
import linecache


def rand_dict(word_length):
    """Generate random words from dictionary of given length.

    word_length: The amount of random words to return.
    returns a list of random words.
    """
    len_dict = 235886
    gen_words = [linecache.getline('/usr/share/dict/words', i)
                 for i in random.sample(range(len_dict), word_length)]
    return gen_words


if __name__ == '__main__':
    setup = '''
import random
import sys
from __main__ import rand_dict
'''
    print(timeit.timeit("''.join(rand_dict(int(sys.argv[1])))",
          setup=setup, number=1000000)/1000000)
    print(rand_dict(int(sys.argv[1])))

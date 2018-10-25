"""This script generate random words from macOS dictionary.

This version uses the default option open(). On my mac it takes around .04
seconds to run.
"""

import random
import sys
import timeit


def rand_dict(word_length):
    f = open('/usr/share/dict/words')
    testf = [i for i in f]
    for i in f:
        testf.append(i)
    f.close()
    rand_sen = random.sample(testf, word_length)
    return rand_sen


if __name__ == '__main__':
    setup = '''
import random
import sys
from __main__ import rand_dict
'''
    print(timeit.timeit("''.join(rand_dict(int(sys.argv[1])))",
          setup=setup, number=1000)/1000)
    # timeit.timeit("rand_dict(10)", setup=setup, number=100)
    print(''.join(rand_dict(int(sys.argv[1]))))

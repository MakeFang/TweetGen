import random
import sys


def rand_dict(word_length):
    f = open('/usr/share/dict/words')
    testf = f.readline()
    f.close()
    return testf


if __name__ == '__main__':
    print(rand_dict(1))

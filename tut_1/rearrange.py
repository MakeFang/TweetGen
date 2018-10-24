import random
import sys


def rearrange(input_words):
    random.shuffle(input_words)
    return input_words


if __name__ == '__main__':
    rearranged = rearrange(sys.argv[1:])
    print(rearranged)

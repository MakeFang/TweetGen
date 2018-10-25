"""This script rearrange a list of words that is given as input.

This version returns a list of rearranged word. It uses another script
implementing Fisher Yates shuffle.
"""

# import random
import sys
import Fisher_Yates


def rearrange(input_words):
    """Return the input words shuffled.

    input_words: a list of input words.
    returns a shuffled list of words.
    """
    # random.shuffle(input_words)
    Fisher_Yates.fisher_yates(input_words)
    return input_words


if __name__ == '__main__':
    rearranged = rearrange(sys.argv[1:])
    print(rearranged)

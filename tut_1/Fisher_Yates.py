"""This script implements the Fisher Yates shuffle.

This version shuffles in place.
"""

import random
import sys


def fisher_yates(input_list):
    """Shuffle the input list described by Fisher-Yates."""
    len_list = len(input_list)
    counter = 1
    while len_list > 0:
        rand_int = random.randint(0, len_list-1)
        input_list[rand_int], input_list[
                    -counter] = input_list[-counter], input_list[rand_int]
        counter += 1
        len_list -= 1
    return input_list


if __name__ == '__main__':
    argument = list(sys.argv[1])
    print(fisher_yates(argument))

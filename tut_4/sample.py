"""This script generates random words given the distribution.

This generating process is done through probability integral transform. It is
acheived through sampling from uniform distribution and solving for the inverse
under its cumulative distribution function. Currently one sampling function
takes 1e-5 seconds on my mac.
"""


import random
import math
import word_frequency
import timeit


def cum_dist(histogram):
    """Compute the cdf given pdf."""
    cumulative = []
    sum = 0
    for i, j in enumerate(histogram):
        sum += j[1]
        cumulative.append((j[0], sum))
    return cumulative


# def binary_search(cumulative, target):
#     cum_len = len(cumulative)
#     res_index = math.floor(cum_len/2)
#     # print("cum", cumulative, "target", target, "index", res_index)
#     if not cumulative:
#         return 0
#     if target == cumulative[res_index][1]:
#         return res_index
#     elif target > cumulative[res_index][1]:
#         return res_index +1 + binary_search(cumulative[res_index+1:], target)
#     else:
#         return binary_search(cumulative[:res_index], target)


def binary_search(cumulative, target):
    """Search throught the list to find target.

    If target is not found,returns the next indexself.
    """
    left = 0
    right = len(cumulative) - 1
    while left < right:
        middle = math.floor((left + right)/2)
        if cumulative[middle][1] == target:
            return middle
        elif cumulative[middle][1] < target:
            left = middle+1
        elif cumulative[middle][1] > target:
            right = middle-1
    return left if target <= cumulative[left][1] else left+1


def sample(cumulative):
    """Generate sample from the distribution."""
    totals = cumulative[-1][1]
    random_int = random.randint(1, totals)
    # index_result = 0
    # for index, item in enumerate(cumulative):
    #     word, num = item
    #     if random_int <= num:
    #         index_result = index
    #         break
    # return cumulative[index_result][0]
    return cumulative[binary_search(cumulative, random_int)][0]


def read_hist():
    """Read the histogram from a txt file."""
    hist = []
    with open('MD_hist.txt', 'r') as f:
        for i in f:
            hist_entry = i.split()
            hist.append((hist_entry[0], int(hist_entry[1])))
    return hist


if __name__ == '__main__':
    # cum = cum_dist(read_hist())
    setup = '''
import random
import math
from __main__ import sample, cum_dist, binary_search, read_hist
cum = cum_dist(read_hist())
'''
    print(timeit.timeit("sample(cum)",
          setup=setup, number=1000000)/1000000)
    # gen_list = [sample(cum) for _ in range(cum[-1][1])]
    # gen_hist = word_frequency.histogram_lt(gen_list)
    # gen_hist_sorted = word_frequency.sort_hist_val(gen_hist)
    # word_frequency.hist_to_file(gen_hist_sorted)

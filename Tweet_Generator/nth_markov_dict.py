# from listogram import SortedListogram, SortedCumugram
from dictogram import Dictogram
from tokenization import read_text_to_list, text_preprocessing
from sample_dict import sample, cumulative_dist
from linkedlist import Node, LinkedList
import random


# def read_markov(word_list, order):
#     markov_dict = {}
#     queue = LinkedList(word_list[:order])
#     for next_word in word_list[order:]:
#         queue_items = tuple(queue.items())
#         if queue_items in markov_dict:
#             markov_dict[queue_items].add_count(next_word)
#         else:
#             markov_dict[queue_items] = Dictogram([next_word])
#         # print(queue)
#         # print(markov_dict)
#         queue.append(next_word)
#         queue.delete(queue.head.data)
#     return markov_dict


def read_markov(word_list, order):
    markov_dict = {}
    starting_dict = Dictogram()
    for sentence in word_list:
        queue = LinkedList(sentence[:order])
        starting_dict.add_count(tuple(queue.items()))
        for next_word in sentence[order:]:
            queue_items = tuple(queue.items())
            if queue_items in markov_dict:
                markov_dict[queue_items].add_count(next_word)
            else:
                markov_dict[queue_items] = Dictogram([next_word])
            # print(queue)
            # print(markov_dict)
            queue.append(next_word)
            queue.delete(queue.head.data)
    return markov_dict, starting_dict


def walk_markov(cur_tuple, markov_dict):
    if cur_tuple in markov_dict:
        # print(markov_dict[cur_tuple])
        return sample(cumulative_dist(markov_dict[cur_tuple]))
    else:
        return None


def get_start(markov_dict):
    start_list = []
    for key in markov_dict.keys():
        if key[0] == 'BOS':
            start_list.append(key)
    return start_list


def gen_sentence(markov_dict, starting_dict, nth):
    # start_tuple = random.choice(list(markov_dict.keys()))
    # start_tuple = random.choice(get_start(markov_dict))
    start_tuple = sample(cumulative_dist(starting_dict))
    cur_list = LinkedList(start_tuple)
    result = LinkedList(start_tuple)
    cur_word = start_tuple[-1]
    # for _ in range(num_words-nth):
    while cur_word != 'EOLS':
        cur_tuple = tuple(cur_list.items())
        new_word = walk_markov(cur_tuple, markov_dict)
        result.append(new_word)
        cur_list.append(new_word)
        cur_list.delete(cur_list.head.data)
        cur_word = new_word
    return result


def main():
    nth = 2
    word_list = read_text_to_list('q.txt')
    markov_dict, starting_dict = read_markov(word_list, nth)
    # print(starting_dict)
    # print(get_start(markov_dict))
    # print(markov_dict)
    # print(walk_markov(('call', 'me'), markov_dict))
    # m_c = read_markov(word_list)
    print(gen_sentence(markov_dict, starting_dict, nth))


if __name__ == '__main__':
    main()

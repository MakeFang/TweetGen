from listogram import SortedListogram, SortedCumugram
from tokenization import read_text, text_preprocessing
from sample import sample, cumulative_dist
from linkedlist import Node, LinkedList
import random


def read_markov(word_list, order):
    markov_dict = {}
    queue = LinkedList(word_list[:order])
    for i in word_list[order:]:
        queue_items = tuple(queue.items())
        if queue_items in markov_dict:
            markov_dict[queue_items].add_count(i)
        else:
            markov_dict[queue_items] = SortedListogram([i])
        # print(queue)
        # print(markov_dict)
        queue.append(i)
        queue.delete(queue.head.data)
    return markov_dict


def walk_markov(cur_tuple, markov_dict):
    if cur_tuple in markov_dict:
        # print(markov_dict[cur_tuple])
        return sample(cumulative_dist(markov_dict[cur_tuple]))
    else:
        return None


def gen_sentence(num_words, markov_dict, nth):
    start_tuple = random.choice(list(markov_dict.keys()))
    cur_list = LinkedList(start_tuple)
    result = LinkedList(start_tuple)
    print(result)
    for _ in range(num_words-nth):
        cur_tuple = tuple(cur_list.items())
        new_word = walk_markov(cur_tuple, markov_dict)
        result.append(new_word)
        cur_list.append(new_word)
        cur_list.delete(cur_list.head.data)
    return result


def main():
    nth = 2
    word_list = text_preprocessing(read_text('pg2489.txt'))
    markov_dict = read_markov(word_list, nth)
    print(walk_markov(('call', 'me'), markov_dict))
    # m_c = read_markov(word_list)
    print(gen_sentence(10, markov_dict, nth))


if __name__ == '__main__':
    main()

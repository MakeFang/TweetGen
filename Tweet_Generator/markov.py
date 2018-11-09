from listogram import SortedListogram, SortedCumugram
from sample import sample
import random


def read_markov(word_list):
    markov_dict = {}
    for i in range(len(word_list)-1):
        if word_list[i] in markov_dict:
            markov_dict[word_list[i]].add_count(word_list[i+1])
        else:
            # markov_dict[word_list[i]] = SortedListogram([word_list[i+1]])
            markov_dict[word_list[i]] = SortedCumugram([word_list[i+1]])
    return markov_dict


def walk_markov(cur_word, markov_dict):
    if cur_word in markov_dict:
        return sample(markov_dict[cur_word])
    else:
        return None


def gen_sentence(num_words, markov_dict):
    cur_word = random.choice(list(markov_dict.keys()))
    result = cur_word
    for _ in range(num_words-1):
        new_word = walk_markov(cur_word, markov_dict)
        result += " " + new_word
        cur_word = new_word
    return result


def main():
    word_list = text_preprocessing(read_text('pg2489.txt'))
    m_c = markov.read_markov(word_list)
    print(gen_sentence(10, m_c))


if __name__ == '__main__':
    print(main())

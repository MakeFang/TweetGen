"""This script generates histograms of word counts for a text.

This script uses three different data structures: dict, list of lists, and list
of tuples. It also provides sorting by key and val.
"""

import re


def read_text():
    """Read the input text."""
    with open('pg2489.txt', 'r') as f:
        text_string = f.read()
    return text_string


def text_preprocessing(source_text):
    """Process the input text."""
    letters = re.sub("[^a-zA-Z'\-]", " ", source_text)
    return letters.lower().split()


def histogram_dict(word_list):
    """Generate a histogram for word counts using dict."""
    hist_dict = {}
    for word in word_list:
        if word in hist_dict:
            hist_dict[word] += 1
        else:
            hist_dict[word] = 1
    return hist_dict


def histogram_ll(word_list):
    """Generate a histogram for word counts using list of lists.

    This function sorts the words first, and then run through the sorted lists
    to populate the histogram.
    """
    word_list.sort()
    histogram = []
    current_word = None
    for text_word in word_list:
        if text_word == current_word:
            histogram[-1][1] += 1
        else:
            histogram.append([text_word, 1])
            current_word = text_word
    return histogram


def histogram_lt(word_list):
    """Generate a histogram for word counts using list of tuple.

    This function sorts the words first, and then run through the sorted lists
    to populate the histogram.
    """
    word_list.sort()
    histogram = []
    current_word = None
    for text_word in word_list:
        if text_word == current_word:
            histogram[-1] = (text_word, histogram[-1][1]+1)
        else:
            histogram.append([text_word, 1])
            current_word = text_word
    return histogram


def unique_words(histogram):
    """Count the number of unique words in the text."""
    return len(histogram)


def frequency(word, histogram):
    """Count the occurance of a word in the text."""
    if type(histogram) == dict:
        if word in histogram:
            return histogram[word]
        else:
            return 0
    elif type(histogram) == list:
        for hist_index, hist_word in enumerate(histogram):
            if word == hist_word[0]:
                return hist_word[1]
        return 0


def sort_hist_val(histogram):
    """Sort the histogram by the counts, ascending."""
    if type(histogram) == dict:
        return sorted(histogram.items(), key=lambda x: x[1], reverse=True)
    elif type(histogram) == list:
        return sorted(histogram, key=lambda x: x[1], reverse=True)


def sort_hist_key(histogram):
    """Sort the histogram by the keys, alphabetically."""
    if type(histogram) == dict:
        return sorted(histogram.items(), key=lambda x: x[0])
    elif type(histogram) == list:
        return sorted(histogram, key=lambda x: x[0])


def hist_to_file(histogram):
    """Write the histogram to a file."""
    with open('MD_hist_gen.txt', 'w') as write_f:
        for words in histogram:
            write_f.write("{0} {1}\n".format(words[0], words[1]))
    return 0


if __name__ == '__main__':
    source_text = read_text()
    word_list = text_preprocessing(source_text)
    print(sort_hist_val(histogram_ll(word_list))[:20])
    print(sort_hist_val(histogram_lt(word_list))[:20])
    print(sort_hist_val(histogram_dict(word_list))[:20])
    hist_to_file(sort_hist_val(histogram_dict(word_list)))

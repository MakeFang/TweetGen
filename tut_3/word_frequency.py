"""This script generates histograms of word counts for a text.

This script uses three different data structures: dict, list of lists, and list
of tuples. It also provides sorting by key and val.
"""

import re


def read_text():
    """Read the input text."""
    # f = open('pg2489.txt', 'r')
    # text_string = f.read()
    # # text_string = f.readlines()
    # # text_string = [i for i in f]
    # # for i in f:
    # #     text_string.append(i.replace('\n', ''))
    # f.close()
    with open('pg2489.txt', 'r') as f:
        text_string = f.read()
    return text_string


def text_preprocessing(source_text):
    """Process the input text."""
    letters = re.sub("[^a-zA-Z'\-]", " ", source_text)
    return letters.lower().split()


def histogram_dict(word_list):
    """Generate a histogram for word counts using dict."""
    # word_list = text_preprocessing(source_text)
    hist_dict = {}
    for i in word_list:
        if i in hist_dict:
            hist_dict[i] += 1
        else:
            hist_dict[i] = 1
    return hist_dict


# def histogram_ll(source_text):
#     word_list = text_preprocessing(source_text)
#     histogram = []
#     for text_word in word_list:
#         for hist_word in histogram:
#             if text_word == hist_word[0]:
#                 hist_word[1] += 1
#                 break
#         else:
#             histogram.append([text_word, 1])
#     return histogram


# def histogram_ll(source_text):
#     hist_dict = histogram_dict(source_text)
#     histogram = []
#     for key, value in hist_dict.items():
#         histogram.append([key, value])
#     return histogram

def histogram_ll(word_list):
    """Generate a histogram for word counts using list of lists.

    This function sorts the words first, and then run through the sorted lists
    to populate the histogram.
    """
    # word_list = text_preprocessing(source_text)
    word_list.sort()
    histogram = []
    currentword = None
    for text_word in word_list:
        if text_word == currentword:
            histogram[-1][1] += 1
        else:
            histogram.append([text_word, 1])
            currentword = text_word
    return histogram

# def histogram_lt(source_text):
#     word_list = text_preprocessing(source_text)
#     histogram = []
#     for text_word in word_list:
#         for hist_index, hist_word in enumerate(histogram):
#             if text_word == hist_word[0]:
#                 histogram[hist_index] = (text_word, hist_word[1]+1)
#                 break
#         else:
#             histogram.append((text_word, 1))
#     return histogram


# def histogram_lt(source_text):
#     hist_dict = histogram_dict(source_text)
#     histogram = []
#     for key, value in hist_dict.items():
#         histogram.append((key, value))
#     return histogram


def histogram_lt(word_list):
    """Generate a histogram for word counts using list of tuple.

    This function sorts the words first, and then run through the sorted lists
    to populate the histogram.
    """
    # word_list = text_preprocessing(source_text)
    word_list.sort()
    histogram = []
    currentword = None
    for text_word in word_list:
        if text_word == currentword:
            histogram[-1] = (text_word, histogram[-1][1]+1)
        else:
            histogram.append((text_word, 1))
            currentword = text_word
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
    with open('MD_hist.txt', 'w') as write_f:
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

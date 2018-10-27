import sys


def read_text():
    """Read the input text."""
    f = open('pg2489.txt', 'r')
    text_string = f.read()
    # text_string = f.readlines()
    # text_string = [i for i in f]
    # for i in f:
    #     text_string.append(i.replace('\n', ''))
    f.close()
    return text_string


def text_preprocessing(source_text):
    return source_text.split()


def histogram_dict(source_text):
    word_list = text_preprocessing(source_text)
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


def histogram_ll(source_text):
    hist_dict = histogram_dict(source_text)
    histogram = []
    for key, value in hist_dict.items():
        histogram.append([key, value])
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


def histogram_lt(source_text):
    hist_dict = histogram_dict(source_text)
    histogram = []
    for key, value in hist_dict.items():
        histogram.append((key, value))
    return histogram


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
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
    if type(histogram) == dict:
        return sorted(histogram.items(), key=lambda x: x[1])
    elif type(histogram) == list:
        return sorted(histogram, key=lambda x: x[1])
    return 0


def sort_hist_key(histogram):
    if type(histogram) == dict:
        return sorted(histogram.items(), key=lambda x: x[0])
    elif type(histogram) == list:
        return sorted(histogram, key=lambda x: x[0])
    return 0


if __name__ == '__main__':
    print(histogram_lt(read_text()))

import random
import sys


def anagram(input_word):
    input_list = list(input_word)
    random.shuffle(input_list)
    return ''.join(input_list)


if __name__ == '__main__':
    anagramed = anagram(sys.argv[1])
    print(anagramed)

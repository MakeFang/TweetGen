import re


def read_text(filename):
    """Read the input text."""
    with open(filename, 'r') as f:
        text_string = f.read()
    return text_string

def read_text_to_list(filename):
    # text_string = []
    with open(filename, 'r') as f:
        # for i in f:
        #     text_string.append(i.replace('\n', ''))
        text_string = [i.replace('\n', '').split() for i in f]
    return text_string

def text_preprocessing(source_text):
    """Process the input text."""
    letters = re.sub("[^a-zA-Z'\-]", " ", source_text)
    return letters.lower().split()


def main():
    filename = 'pg2489.txt'
    return text_preprocessing(read_text(filename))[:20]


if __name__ == '__main__':
    print(main())

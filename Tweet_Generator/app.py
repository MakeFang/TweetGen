"""This is a Flask simple website.

It will be filled with generating random words.
"""
from flask import Flask, render_template, request
# import sample
from tokenization import read_text_to_list, text_preprocessing
# from listogram import SortedListogram, SortedCumugram
import nth_markov_dict
app = Flask(__name__)

# app.cumulative_dist instead
app.nth = 2
app.word_list = read_text_to_list('q.txt')
app.markov, app.starting = nth_markov_dict.read_markov(app.word_list, app.nth)
# app.markov = markov.read_markov(app.word_list)
# app.histogram = SortedListogram(app.word_list)
# app.cumulative_dist = sample.cumulative_dist(app.histogram)


@app.route('/')
def gen_words():
    # num_words = int(request.args.get('num')) if request.args.get('num') else 10
    result = nth_markov_dict.gen_sentence(app.markov, app.starting, app.nth)
    result = ' '.join(result.items()[1:-1])
    return render_template('index.html', result=result)

# def gen_words():
#     result = ''
#     num_words = int(request.args.get('num')) if request.args.get('num') else 10
#     for _ in range(num_words):
#         result += sample.sample(app.cumulative_dist) + ' '
#     return render_template('index.html', result=result)

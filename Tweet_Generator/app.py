"""This is a Flask simple website.

It will be filled with generating random words.
"""
from flask import Flask, render_template, request
import sample
app = Flask(__name__)


cumulative_dist = sample.cumulative_dist(sample.read_hist())


@app.route('/')
def gen_words():
    result = ''
    num_words = int(request.args.get('num')) if request.args.get('num') else 10
    for _ in range(num_words):
        result += sample.sample(cumulative_dist) + ' '
    return render_template('index.html', result=result)

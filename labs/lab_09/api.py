# CMPT 120 Intro to Programming
# Lab #9 - Working with APIs
# Author: Harrison Zheng
# Date: 2019-11-27


import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Hello, world!"


books = [
    {
        'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '1992'
    },
    {
        'id': 1,
        'title': 'The ones who walk away from Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows \
            soaring, the Festival of Summer came to the city Omelas, \
            bright-towered by the sea.',
        'year_published': '1973'
    },
    {
        'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'
    }
]


@app.route('/api/books/all', methods=['GET'])
def get_all_books():
    return jsonify(books)


@app.route('/api/books', methods=['GET'])
def get_book():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No ID field provided. Please specify an ID."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)
    return jsonify(results)


@app.errorhandler(404)
def page_not_found(e):
    return "404 - The resource could not be found.", 404


app.run()

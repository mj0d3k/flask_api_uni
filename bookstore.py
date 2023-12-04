from flask import Flask
import json

bookstore = Flask(__name__)


with open('books.json') as json_data:
    result = []
    data = json.load(json_data)
    for book in data['books']:



if __name__ == '__main__':
    bookstore.run(debug=True)

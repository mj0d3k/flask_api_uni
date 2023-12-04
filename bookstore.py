from flask import Flask, jsonify
import json

bookstore = Flask(__name__)





if __name__ == '__main__':
    bookstore.run(debug=True)

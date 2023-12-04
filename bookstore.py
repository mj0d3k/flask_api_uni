from flask import Flask

bookstore = Flask(__name__)

@bookstore.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    bookstore.run(debug=True)

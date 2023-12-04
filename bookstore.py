from flask import Flask, jsonify, request
import json

bookstore = Flask(__name__)

with open('books.json') as json_data:
    result = []
    data = json.load(json_data)
    for book in data['books']:
        result.append(book['isbn'])


def validate_publisher_param():
    publisher = request.args.get('publisher')
    if not publisher:
        response = jsonify({'error': 'Provide a publisher.'})
        return response, 400
    return None, None


def validate_isbn_param(isbn):
    for book in data['books']:
        if book['isbn'] == isbn:
            return None, None
    response = jsonify({'error': 'Book not found'})
    return response, 404


@bookstore.route("/isbns", methods=['GET'])
def get_all_isbns():
    return jsonify([book['isbn'] for book in data['books']])


@bookstore.route('/isbns/<isbn>', methods=['GET'])
def get_book_by_isbn(isbn):
    response, status_code = validate_isbn_param(isbn)
    if response:
        return response, status_code

    for book in data['books']:
        if book['isbn'] == isbn:
            return jsonify(book)

    return jsonify({'error': 'Book not found'}), 404


@bookstore.route('/authors/<expression>', methods=['GET'])
def get_authors_by_expression(expression):
    authors = [book['author'] for book in data['books'] if expression.lower() in book['title'].lower()]
    return jsonify(authors)


@bookstore.route('/isbns/<isbn>', methods=['PUT'])
def publisher_update(isbn):
    response, status_code = validate_publisher_param()
    if response:
        return response, status_code

    updated_books = []
    for book in data['books']:
        if book['isbn'] == isbn:
            book['publisher'] = request.args.get('publisher')
        updated_books.append(book)

    if any(book['isbn'] == isbn and 'publisher' in book for book in updated_books):
        data['books'] = updated_books
        return jsonify({'message': f'Publisher for ISBN {isbn} updated to {request.args.get("publisher")}.'})
    else:
        return jsonify({'error': f'Book with ISBN {isbn} not found.'}), 404


if __name__ == "__main__":
    bookstore.run(debug=True)

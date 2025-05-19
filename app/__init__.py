from flask import Flask, jsonify, request
from app.services import library_service

def create_app():
    app = Flask(__name__)

    @app.route("/hello", methods=["GET"])
    def hello():
        return "api", 200

    @app.route('/api/v1/books', methods=["GET"])
    def get_books():
        books = library_service.get_books()
        return jsonify({'books': books}), 200    

    @app.route('/api/v1/books', methods=['POST'])
    def create_book():
        try:
            data = request.get_json()
            isbn = data.get('isbn')
            title = data.get('title')
            copies = data.get('copies', 1)
            library_service.create_book(isbn, title, copies)
            return jsonify({'message': 'Book created successfully'}), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'Server error'}), 500

    @app.route('/api/v1/books/<isbn>', methods=['PUT'])
    def update_book(isbn):
        try:
            data = request.get_json()
            title = data.get('title')
            copies = data.get('copies', 1)
            library_service.update_book(isbn, title, copies)
            return jsonify({'message': 'Book updated successfully'}), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'Server error'}), 500

    @app.route('/api/v1/books/<isbn>', methods=['DELETE'])
    def delete_book(isbn):
        try:
            library_service.delete_book(isbn)
            return jsonify({'message': 'Book deleted successfully'}), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'Server error'}), 500
    return app
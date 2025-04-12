from flask import Flask, jsonify
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
    return app
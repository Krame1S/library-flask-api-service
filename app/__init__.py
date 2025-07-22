from flask import Flask
from app.api import routes

def create_app():
    app = Flask(__name__)
    routes.register_routes(app)
    return app

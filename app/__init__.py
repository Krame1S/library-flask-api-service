from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/hello", methods=["GET"])
    def hello():
        return "api", 200
    
    return app
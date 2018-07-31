from flask import Flask

def create_app():
    app = Flask(__name__)

    from .blueprints import admin
    app.register_blueprint(admin)
    return app

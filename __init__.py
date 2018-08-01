from flask import Flask

def create_app(config_file=None):

    app = Flask(__name__)

    if app.config['DEBUG']:
        from . import settings
        app.config.from_object(settings)
    else:
        app.config.from_pyfile(config_file)
    from .blueprints import admin
    app.register_blueprint(admin)
    return app

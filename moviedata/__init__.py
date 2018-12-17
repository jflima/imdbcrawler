import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint="index")

    return app
from .views import views
from .auth import auths
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456789'

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auths, url_prefix='/')

    return app

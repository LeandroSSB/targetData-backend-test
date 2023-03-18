from flask import Flask
from app.routes.user_blueprint import bp as user_blueprint


def init_app(app: Flask):
    app.register_blueprint(user_blueprint)

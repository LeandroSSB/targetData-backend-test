from environs import Env
from flask import Flask

env = Env()
env.read_env()


def init_app(app):
    app.config["MONGO_URI"] = env("MONGO_URI")
    # app.config[]

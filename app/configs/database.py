from flask_pymongo import PyMongo
from flask import Flask
from environs import Env

env = Env()
env.read_env()

mongo = PyMongo()


def init_app(app: Flask):
    mongo.init_app(app)


def get_db() -> PyMongo():
    return mongo.db[env("DATABASE")]

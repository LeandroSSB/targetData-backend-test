from flask import Flask, jsonify
from app.configs import env_config as env, database
from app import routes


def create_app():

    app = Flask(__name__)
    if __name__ == '__main__':
        app.run(host='0.0.0.0')
    env.init_app(app)
    # routes.init_app(app)
    database.init_app(app)

    @app.get("/")
    def home():
        return jsonify({"greet": "welcome to my flask application"}), 200

    return app

import os
from flask import Flask
from models import setup_db
from flask_cors import CORS


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello"
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"


    @app.route('/actors')
    def get_actors():
        return "Be cool, man, be coooool! You're almost a FSND grad!"


    @app.route('/actors/<int:id>', methods=['DELETE'])
    def remove_actors(id):
        return "Be cool, man, be coooool! You're almost a FSND grad!"


    @app.route('/movies')
    def get_movies():
        return "Be cool, man, be coooool! You're almost a FSND grad!"


    @app.route('/movies/<int:id>', methods=['DELETE'])
    def remove_movies(id):
        return "Be cool, man, be coooool! You're almost a FSND grad!"


    return app

app = create_app()

if __name__ == '__main__':
    app.run()
from flask import Flask


def create_app():
    app = Flask(__name__)
    # secure cookies and session data
    app.config['SECRET_KEY'] = 'a5#$#1342353223424$d5658*(&*(sa1dsa5d14S5¨&5d1$@2D#@4-54d1'

    return app



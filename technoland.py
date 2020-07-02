import os
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, Config, logging

app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


from distutils.log import debug
import mimetypes
from flask import Flask, send_file, redirect
APP = Flask(__name__)


@APP.route("/")
def home():
    return "Hello World!"


@APP.route("/rickroll")
def rick_roll():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")


@APP.route("/cat")
def get_cat():
    return send_file('./cat.jpg', mimetype='image/jpg')


if __name__ == "__main__":
    APP.run(port=10000, debug=True)

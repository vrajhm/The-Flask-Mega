from lecture2 import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Vraj"}
    posts = [
        {
            "author" : {"username": "John"},
            "body" : "What a day to be alive"
        },

        {
            "author" : {"username": "Susan"},
            "body" : "It's a nice summer day!"
        }
    ]
    return render_template("index.html", title = "Home", user = user, posts = posts)
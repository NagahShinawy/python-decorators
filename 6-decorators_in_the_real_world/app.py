"""
created by Nagaj at 31/07/2021
"""
# set FLASK_APP=app.py    ===> windows
# export FLASK_APP=app.py    ===> linux


from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/users/<user>")
def users(user):
    h1 = "<h5 style='color:red;'>{user}</h5>"
    return h1.format(user=user)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, use_reloader=True)

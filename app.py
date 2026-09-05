from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! My Dockerized Flask Application is Working!"


@app.route("/about")
def about():
    return "This application was created using Flask, Docker and GitHub."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
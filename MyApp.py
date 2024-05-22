from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/abhi", methods = ["GET", "POST"])
def abhi():
    return "ok"


if __name__ == "__main__":
    app.run()
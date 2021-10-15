



from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello there<h1>"

@app.route("/<name>")
def user(name):
    return "Hello " + name

if __name__ == "__main__":
    app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'snail remote control API'

if __name__ == "__main__":
    app.run()

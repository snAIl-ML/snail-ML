from flask import Flask
from controller import Controller

app = Flask(__name__)

controller = Controller()

@app.route("/")
def index():
    return 'snail remote control API'

@app.route("/forward")
def forward():
    controller.up()
    return 'forward'

if __name__ == "__main__":
    app.run()

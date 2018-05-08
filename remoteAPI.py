from flask import Flask
from controller import Controller

app = Flask(__name__)

controller = Controller()

@app.route("/")
def index():
    controller.create_temp_photo()
    return 'snail remote control API'

@app.route("/forward")
def forward():
    controller.up()
    return 'forward'

@app.route("/piv_left")
def piv_left():
    controller.piv_left()
    return "piv_left"

@app.route("/piv_right")
def piv_right():
    controller.piv_right()
    return "piv_right"

if __name__ == "__main__":
    app.run()

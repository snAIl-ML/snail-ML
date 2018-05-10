'Remote API Module'
from flask import Flask, render_template, redirect
from controller import Controller

APP = Flask(__name__, static_url_path='', static_folder='images/current_image')

CONTROLLER = Controller()

@APP.route("/")
def index():
    'Function for main route'
    CONTROLLER.create_temp_photo()
    return render_template('index.html', image_path=CONTROLLER.get_photoname())

@APP.route("/forward")
def forward():
    'Function for forward command'
    CONTROLLER.up()
    return redirect('/')

@APP.route("/piv_left")
def piv_left():
    'Function for left command'
    CONTROLLER.piv_left()
    return redirect('/')

@APP.route("/piv_right")
def piv_right():
    'Function for right command'
    CONTROLLER.piv_right()
    return redirect('/')

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=5000)

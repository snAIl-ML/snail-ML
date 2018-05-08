from flask import Flask, render_template, url_for
from controller import Controller

app = Flask(__name__, static_url_path='', static_folder='images/current_image')

controller = Controller()

@app.route("/")
def index():
    controller.create_temp_photo()
    return render_template ('index.html', image_path = controller.get_photoname())

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

from flask import Flask, render_template, url_for, redirect
from controller import Controller
from ai_checker import AIChecker
from get_move_from_server import get_server_move
from snail import get_img_path

app = Flask(__name__, static_url_path='', static_folder='images/current_image')
controller = Controller()
URL = "http://192.168.48.206:8000/upload"
@app.route("/")
def index():

    controller.create_temp_photo()
    return render_template ('index.html', image_path = controller.get_photoname())

@app.route("/forward")
def forward():
    controller.up()
    return redirect('/')

@app.route("/piv_left")
def piv_left():
    controller.piv_left()
    return redirect('/')

@app.route("/piv_right")
def piv_right():
    controller.piv_right()
    return redirect('/')

@app.route("/ai_move")
def run_ai():
    print("ai route running AI")
    controller.create_temp_photo()
    move = get_server_move(get_img_path(), URL)
    print(move)
    if move == 'forward': controller.up()
    elif move == 'pivot right': controller.piv_right()
    else: controller.piv_left()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

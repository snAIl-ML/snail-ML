from flask import Flask, render_template, url_for, redirect, request
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
def ai_mode():
    "this route is expected to be called with the"
    "origins ML image upload URL as a query param"
    host_url = request.args['host_url']
    controller.create_temp_photo()
    img_path = controller.get_img_path()
    move = controller.get_server_move(img_path, host_url)
    if move == 'forward': controller.up()
    elif move == 'pivot right': controller.piv_right()
    else: controller.piv_left()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

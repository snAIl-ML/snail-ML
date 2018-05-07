import path_helper_main_ml
from label_image_no_cli import classify_image
from controller import Controller
import os
from get_move_from_server import get_server_move

URL = "WHERE"

def user_loop(control=Controller):
    w = control()
    w.create_temp_photo()
    w.start_turtle()
    w.window.onkey(w.up, 'Up')
    w.window.onkey(w.down, 'Down')
    w.window.onkey(w.right, 'Right')
    w.window.onkey(w.left, 'Left')
    w.window.onkey(w.piv_right, 'l')
    w.window.onkey(w.piv_left, 'k')
    w.window.onkey(w.exit_turtle, 'q')
    w.window.listen()
    turtle.mainloop()

def user_supervision():
    get_mode = input("Continue AI driving? 1 = Yes, 2 = No:  ")
    if get_mode == "1": AI_loop()

def get_img_path():
    return "./images/current_image/" + os.listdir("./images/current_image")[0]

def AI_loop(counter=5, ai=get_server_move, user=user_supervision, img_path=get_img_path, control=Controller):
    con = control()
    con.create_temp_photo()
    while counter>0:
        move = ai(URL, img_path())
        if move == 'forward': con.up()
        elif move == 'pivot right': con.piv_right()
        else: con.piv_left()
        counter -= 1
    return user()

def set_mode():
    get_mode = input("Choose mode: 1 = User, 2 = AI: ")
    if get_mode == "1": user_loop()
    if get_mode == "2": AI_loop()

if __name__ == "__main__":
   set_mode()

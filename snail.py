'Main module'
import os
import turtle
from controller import Controller
from get_move_from_server import get_server_move


URL = "http://192.168.48.116:8000/upload"

def user_loop(control=Controller):
    'Loop for RC'
    w = control()
    w.create_temp_photo()
    w.start_turtle()
    w.window.onkey(w.up, 'Up')
    w.window.onkey(w.down, 'Down')
    w.window.onkey(w.right, 'r')
    w.window.onkey(w.left, 'l')
    w.window.onkey(w.piv_right, 'Right')
    w.window.onkey(w.piv_left, 'Left')
    w.window.onkey(w.exit_turtle, 'x')
    w.window.listen()
    turtle.mainloop()

def user_supervision():
    'Control to continue or stop'
    get_mode = raw_input("Continue AI driving? 1 = Yes, 2 = No:  ")
    if get_mode == "1": AI_loop()

def get_img_path():
    'Obtain image route'
    return "./images/current_image/" + os.listdir("./images/current_image")[0]

def set_server_url():
    'Set the server url'
    URL = raw_input("Enter AI server URL: ")

def AI_loop(
        counter=100,
        ai=get_server_move,
        user=user_supervision,
        img_path=get_img_path,
        control=Controller
    ):
    'Loop for AI'
    con = control() # BE NICE NOT TO MAKE A NEW CONTROLLER EVERY LOOP?
    con.create_temp_photo()
    while counter>0:
        move = ai(img_path(), URL)
        print("move ======== ", move)
        if move == 'forward':
            con.up()
        elif move == 'pivot right':
            con.piv_right()
        else:
            con.piv_left()
        counter -= 1
    return user()

def set_mode():
    'Choose RC mode or AI more'
    get_mode = raw_input("Choose mode: 1 = User, 2 = AI: ")
    if get_mode == "1": user_loop()
    elif get_mode == "2":
        set_server_url()
        AI_loop()

if __name__ == "__main__":
   set_mode()

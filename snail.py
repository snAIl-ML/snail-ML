'Main module'
import os
import turtle
from controller import Controller
from get_move_from_server import get_server_move


URL = "http://192.168.48.116:8000/upload"

def user_loop(control=Controller):
    'Loop for RC'
    pannel = control()
    pannel.create_temp_photo()
    pannel.start_turtle()
    pannel.window.onkey(pannel.up, 'Up')
    pannel.window.onkey(pannel.down, 'Down')
    pannel.window.onkey(pannel.right, 'r')
    pannel.window.onkey(pannel.left, 'l')
    pannel.window.onkey(pannel.piv_right, 'Right')
    pannel.window.onkey(pannel.piv_left, 'Left')
    pannel.window.onkey(pannel.exit_turtle, 'x')
    pannel.window.listen()
    turtle.mainloop()

def user_supervision():
    'Control to continue or stop'
    get_mode = raw_input("Continue AI driving? 1 = Yes, 2 = No:  ")
    if get_mode == "1":
        ai_loop()

def get_img_path():
    'Obtain image route'
    return "./images/current_image/" + os.listdir("./images/current_image")[0]

def set_server_url():
    'Set the server url'
    URL = raw_input("Enter AI server URL: ")

def ai_loop(
        counter=100,
        artificial_intelligence=get_server_move,
        user=user_supervision,
        img_path=get_img_path,
        control=Controller
    ):
    'Loop for AI'
    con = control() # BE NICE NOT TO MAKE A NEW CONTROLLER EVERY LOOP?
    con.create_temp_photo()
    while counter > 0:
        move = artificial_intelligence(img_path(), URL)
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
    if get_mode == "1":
        user_loop()
    elif get_mode == "2":
        set_server_url()
        ai_loop()

if __name__ == "__main__":
    set_mode()

import path_helper_main_ml
from label_image_no_cli import classify_image
from controller import Controller

def user_loop():
    w = Controller()
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
    pass

def AI_loop(counter=5, ai=classify_image, user=user_supervision):
    con = Controller()
    con.create_temp_photo()

def set_mode():
    get_mode = raw_input("Choose mode: 1 = User, 2 = AI: ")
    if get_mode == "1": user_loop()
    if get_mode == "2":
        print ("AI mode isn't written yet!")
        set_mode()

if __name__ == "__main__":
   set_mode()

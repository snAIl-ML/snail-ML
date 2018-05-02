import tty
import sys
import termios
import car as car
import camera

class Controller(object):

    def __init__(self, car=car, cam=camera):
        self.cam = cam
        self.photo_path = "replace me"
        self.car = car

    def create_temp_photo(self):
        img_data = self.cam.grab_image_data()
        dir_path = self.cam.create_path("current_image")
        self.cam.create_directory(dir_path)
        self.photo_path = self.cam.save_photo(dir_path, img_data)

    def up(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("forward")
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.forward(0.2)
        self.create_temp_photo()

    def down(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("reverse")
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.reverse(0.2)
        self.create_temp_photo()

    def right(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("turn_right")
        self.cam.create_directory(new_path)
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.turn_right(0.2)
        self.create_temp_photo()

    def left(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("turn_left")
        self.cam.create_directory(new_path)
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.turn_left(0.2)
        self.create_temp_photo()

    def piv_right(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("pivot_right")
        self.cam.create_directory(new_path)
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.pivot_right(0.2)
        self.create_temp_photo()

    def piv_left(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("pivot_left")
        self.cam.create_directory(new_path)
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.pivot_left(0.2)
        self.create_temp_photo()

def user_control_loop():
    #Backing up original attributes
    orig_settings = termios.tcgetattr(sys.stdin)
    #Setting up stdin in raw
    tty.setraw(sys.stdin)
    C = Controller()
    C.create_temp_photo()
    comm = 0
    while comm != "x":
        comm =  sys.stdin.read(1)[0]
        if comm == "w": C.up()
        elif comm == "s": C.down()
        elif comm == "a": C.left()
        elif comm == "d": C.right()
        elif comm == "q": C.piv_left()
        elif comm == "e": C.piv_right()

    #Restoring original attributes of stdin
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

def set_mode():
    get_mode = input("chose mode: 1 = user, 2 = AI ")
    if get_mode == "1": user_control_loop()
    if get_mode == "2":
        print ("AI mode isn't written yet!")
        set_mode()

if __name__ == "__main__":
   set_mode()

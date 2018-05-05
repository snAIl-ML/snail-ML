import sys
import car as car
import camera
import turtle
import time # to see processing time
import cv2

class Controller(object):

    def __init__(self, car=car, cam=camera, vision = cv2):
        self.camera_object = vision.VideoCapture(0)
        self.cam = cam
        self.photo_path = "current_image/test_string"
        self.car = car

    def get_photoname(self):
        return self.photo_path.split("/")[-1]

    def create_temp_photo(self):
        start_time = time.time()
        img_data = self.cam.grab_image_data(self.camera_object)
        dir_path = self.cam.create_return_path("current_image")
        self.photo_path = self.cam.save_photo(dir_path, img_data)
        print ("create temp photo took: ", time.time() - start_time, "seconds")


    def up(self):
        start_time = time.time()
        new_path = self.cam.create_return_path("forward")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.forward(0.2)
        self.create_temp_photo()
        print ("A move inc moving photo and creating photo took: ", time.time() - start_time, "seconds")

    def down(self):
        new_path = self.cam.create_return_path("reverse")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.reverse(0.2)
        self.create_temp_photo()

    def right(self):
        new_path = self.cam.create_return_path("turn_right")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.turn_right(0.2)
        self.create_temp_photo()

    def left(self):
        new_path = self.cam.create_return_path("turn_left")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.turn_left(0.2)
        self.create_temp_photo()

    def piv_right(self):
        new_path = self.cam.create_return_path("pivot_right")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.pivot_right(0.2)
        self.create_temp_photo()

    def piv_left(self):
        new_path = self.cam.create_return_path("pivot_left")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.pivot_left(0.2)
        self.create_temp_photo()

    def start_turtle(self):
        turtle.setup(400,500)
        self.window = turtle.Screen()
        self.window.title('snAIl Controller')
        self.window.bgcolor('blue')

    def exit_turtle(self):
        del(self.camera_object)
        self.clear_current_image_folder()
        self.window.bye()

    def clear_current_image_folder(self):
        self.cam.delete_current_photo()

def turtle_loop():
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

def set_mode():
    get_mode = input("Choose mode: 1 , 2 = AI: ")
    if get_mode == "1": turtle_loop()
    if get_mode == "2":
        print ("AI mode isn't written yet!")
        set_mode()

if __name__ == "__main__":
   set_mode()

import car
import camera
import turtle
import cv2

class Controller(object):

    PHOTO_WIDTH = 320
    PHOTO_HEIGHT = 240
    TIME_FRAME = 0.2
    USER_CONTROLLER_WIDTH = 400
    USER_CONTROLLER_HEIGHT = 500

    def __init__(self, car=car, cam=camera, vision = cv2):
        self.cam_object = vision.VideoCapture(0)
        self.cam_object.set(3, self.PHOTO_WIDTH)
        self.cam_object.set(4, self.PHOTO_HEIGHT)
        self.cam = cam
        self.photo_path = "current_image/test_string"
        self.car = car

    def get_photoname(self):
        return self.photo_path.split("/")[-1]

    def create_temp_photo(self):
        self.cam.delete_current_photo()
        img_data = self.cam.grab_image_data(self.cam_object)
        dir_path = self.cam.create_return_path("current_image")
        self.photo_path = self.cam.save_photo(dir_path, img_data)

    def up(self):
        new_path = self.cam.create_return_path("forward")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.forward(self.TIME_FRAME)
        self.create_temp_photo()

    def down(self):
        new_path = self.cam.create_return_path("reverse")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.reverse(self.TIME_FRAME)
        self.create_temp_photo()

    def right(self):
        new_path = self.cam.create_return_path("turn_right")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.turn_right(self.TIME_FRAME)
        self.create_temp_photo()

    def left(self):
        new_path = self.cam.create_return_path("turn_left")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.turn_left(self.TIME_FRAME)
        self.create_temp_photo()

    def piv_right(self):
        new_path = self.cam.create_return_path("pivot_right")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.pivot_right(self.TIME_FRAME)
        self.create_temp_photo()

    def piv_left(self):
        new_path = self.cam.create_return_path("pivot_left")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.pivot_left(self.TIME_FRAME)
        self.create_temp_photo()

    def start_turtle(self):
        turtle.setup(self.USER_CONTROLLER_WIDTH, self.USER_CONTROLLER_HEIGHT)
        self.window = turtle.Screen()
        self.window.title('snAIl Controller')
        self.window.bgcolor('#e8e8e8')
        self.window.bgpic('./logo/logo.gif')

    def exit_turtle(self):
        del(self.cam_object)
        self.window.bye()

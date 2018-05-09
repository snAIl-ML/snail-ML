import car
import camera
import turtle
import cv2
import os
import requests

class Controller(object):

    PHOTO_WIDTH = 320
    PHOTO_HEIGHT = 240
    FWD_TIME_FRAME = 0.2
    PIV_TIME_FRAME = 0.1
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
        print("forwards count = " +
        str(len(os.listdir("./images/forward"))))
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.forward(self.FWD_TIME_FRAME)
        self.create_temp_photo()

    def down(self):
        new_path = self.cam.create_return_path("reverse")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.reverse(self.FWD_TIME_FRAME)
        self.create_temp_photo()

    def right(self):
        new_path = self.cam.create_return_path("turn_right")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.turn_right(self.FWD_TIME_FRAME)
        self.create_temp_photo()

    def left(self):
        new_path = self.cam.create_return_path("turn_left")
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.turn_left(self.FWD_TIME_FRAME)
        self.create_temp_photo()

    def piv_right(self):
        new_path = self.cam.create_return_path("pivot_right")
        print("pivot right count = " +
        str(len(os.listdir("./images/pivot_right"))))
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.pivot_right(self.PIV_TIME_FRAME)
        self.create_temp_photo()

    def piv_left(self):
        new_path = self.cam.create_return_path("pivot_left")
        print("pivot left count = " +
        str(len(os.listdir("./images/pivot_left"))))
        self.cam.move_photo(self.photo_path, new_path + "/" + self.get_photoname())
        self.car.pivot_left(self.PIV_TIME_FRAME)
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

    def get_server_move(image_path, url):
        'Function to get response from the server'
        server_move = requests.post(url, files={'image': open(image_path, 'rb')})
        return server_move.text

    def get_img_path():
        return "./images/current_image/" + os.listdir("./images/current_image")[0]

from datetime import datetime
import time
import cv2
import os

def grab_image_data(vision = cv2):
    cam = vision.VideoCapture(0)
    time.sleep(0.1)
    image = cam.read()
    del(cam)
    return image[1]

def create_path(action):
    print(os.path.dirname)
    return os.path.join('images', action)

def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def save_photo(dir_path, image_data, vision = cv2):
    image_name_and_path = dir_path + '/' + str(datetime.now().strftime('%Y-%m-%d %H-%M-%S')) + '.png'
    vision.imwrite(image_name_and_path, image_data)

def move_photo(old_path, new_path):
    os.rename(old_path, new_path)

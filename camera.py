import time
import cv2
import os

def grab_image_data(vision = cv2):
    cam = vision.VideoCapture(0)
    time.sleep(0.1)
    image = cam.read()
    del(cam)
    return image[1]

def create_return_path(action):
    return create_directory(get_path(action))

def get_path(action):
    return os.path.join('images', action)

def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

def save_photo(dir_path, image_data, vision=cv2):
    image_name_and_path = (dir_path + '/' +
        time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()) + '.png')
    vision.imwrite(image_name_and_path, image_data)
    return image_name_and_path

def move_photo(old_path, new_path):
    os.rename(old_path, new_path)

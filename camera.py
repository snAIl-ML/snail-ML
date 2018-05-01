from datetime import datetime
import time
import cv2
import os

def take_photo(vision = cv2):
    cam = vision.VideoCapture(0)
    image = cam.read()
    del(cam)
    return image[1]

def create_path(action):
    print(os.path.dirname)
    return os.path.join('images', action)

def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

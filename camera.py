import time
import cv2
import os

def grab_image_data(cam_object):
    image = ''
    for i in range(0,2):
        image = cam_object.read()
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
        time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()) + '.jpg')
    vision.imwrite(image_name_and_path, image_data)
    return image_name_and_path

def move_photo(old_path, new_path):
    os.rename(old_path, new_path)

def delete_current_photo(path="./images/current_image"):
    if os.path.exists(path):
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))

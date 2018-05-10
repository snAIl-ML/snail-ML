'Camera Module'
import os
import time
import cv2


def grab_image_data(cam_object):
    'Function grab image data'
    image = ''
    # W: 10, 8: Unused variable 'i' (unused-variable)
    for i in range(0, 2):
        image = cam_object.read()
    return image[1]

def create_return_path(action):
    'Function create return path'
    return create_directory(get_path(action))

def get_path(action):
    'Function get path'
    return os.path.join('images', action)

def create_directory(dir_path):
    'Function create directory'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

def save_photo(dir_path, image_data, vision=cv2):
    'Function save photo'
    image_name_and_path = (dir_path + '/' +
                           time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()) + '.jpg')
    vision.imwrite(image_name_and_path, image_data)
    return image_name_and_path

def move_photo(old_path, new_path):
    'Function move photo'
    os.rename(old_path, new_path)

def delete_current_photo(path="./images/current_image"):
    'Function delete current photo'
    if os.path.exists(path):
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))

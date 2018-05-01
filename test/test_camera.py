import context
from mock import patch
import camera
import time
import os

class mock_camera(object):

    def read(self):
        return [True, 'image']

    def release_camera(self, cam):
        return True

    def release(self):
        return True

class mock_image_handler(object):

    def VideoCapture(self):
        return mock_camera()

    def read_from_camera(self, cam):
        return [True, 'image']

def test_take_photo():
    assert(camera.take_photo(mock_image_handler)) == 'image'

def test_create_path():
    assert(camera.create_path('forward')) ==  'images/forward'

def test_create_directory():
    camera.create_directory('test')
    assert(os.path.exists('test')) == True
    pass

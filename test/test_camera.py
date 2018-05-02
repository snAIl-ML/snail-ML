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

    def imwrite(image_name, image_data):
        return True

def test_create_directory(mocker):
    def save_photo(makedirs):
        os.makedirs('directory_path')
    stub = mocker.stub(name='os.makedirs')
    camera.create_directory(stub)
    stub.assert_called_once_with('directory_path')
    pass

def test_grab_image_data():
    assert(camera.grab_image_data(mock_image_handler)) == 'image'

def test_create_path():
    assert(camera.create_path('forward')) ==  'images/forward'

def test_create_directory():
    camera.create_directory('test directory')
    assert(os.path.exists('test directory')) == True
    os.rmdir('test directory')

def test_save_photo():
    assert(camera.save_photo('dir_path', 'image_data', mock_image_handler)) == True

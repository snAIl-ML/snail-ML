import context
import pytest
from pytest_mock import mocker
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

def test_create_directory_creates_image_directory_if_doesnt_exist(mocker):
    mocker.patch.object(os, 'makedirs')
    camera.create_directory('test directory')
    os.makedirs.assert_called

def test_grab_image_data():
    assert(camera.grab_image_data(mock_image_handler)) == 'image'

def test_create_path():
    assert(camera.create_path('forward')) ==  'images/forward'

def test_save_photo(mocker):
    mocker.patch.object(mock_image_handler, 'imwrite')
    camera.save_photo('dir_path', 'image_data', mock_image_handler)
    mock_image_handler.imwrite.assert_called

def test_move_photo(mocker):
    mocker.patch.object(os, 'rename')
    camera.move_photo('this', 'that')
    os.rename.assert_called

import context
import pytest
from unittest.mock import patch
from pytest_mock import mocker
import camera
from datetime import datetime
import time
import os

faketimenow = time.localtime(time.mktime((2018, 1, 1, 0, 3, 0, 0, 1, 0)))

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
    assert os.makedirs.called

def test_grab_image_data():
    assert(camera.grab_image_data(mock_image_handler)) == 'image'

def test_get_path_returns_a_path():
    assert(camera.get_path('forward')) ==  'images/forward'

def test_create_return_path_returns_path_and_creates_image_directory_if_doesnt_exist(mocker):
    mocker.patch.object(os, 'makedirs')
    assert(camera.create_return_path('path')) ==  "images/path"


def test_save_photo(mocker):
    mocker.patch.object(mock_image_handler, 'imwrite')
    camera.save_photo('dir_path', 'image_data', mock_image_handler)
    mock_image_handler.imwrite.assert_called

@patch('time.localtime')
def test_save_photo_returns_the_save_path(mock_time):
    mock_time.return_value = faketimenow
    timestring = time.strftime('%Y-%m-%d %H-%M-%S', faketimenow)
    assert(
        camera.save_photo('dir_path', 'image_data', mock_image_handler)
    ) == "dir_path/" + timestring + ".jpg"

def test_move_photo(mocker):
    mocker.patch.object(os, 'rename')
    camera.move_photo('this', 'that')
    assert os.rename.called

def test_delete_current_photo_deletes_all_files_in_dir():
    os.makedirs("testing_remove")
    os.chdir("./testing_remove")
    text_file = open("test_file.txt", "w")
    text_file.write("test_string")
    text_file.close()
    camera.delete_current_photo(".")
    assert 'test_file' not in os.listdir(".")
    os.chdir("..")
    os.rmdir("testing_remove")

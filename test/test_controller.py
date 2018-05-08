import path_helper_test_main
from controller import Controller
import mock
import pytest
from pytest_mock import mocker
import camera
import car

class mock_camera(object):

    def __init__(self):
        self.paths = []
        self.test_string = "test"

    def grab_image_data(self, cam_object):
        return True

    def create_path(self, x):
        return x

    def create_directory(self, x):
        pass

    def save_photo(self, x, y):
        return "a string"

    def move_photo(self, old_path, new_path):
        self.paths = [old_path, new_path]

    def create_return_path(self, path):
        return path

    def delete_current_photo(self):
        self.test_string = "deleted"

    def create_temp_photo():
        return True

    def set(self, x, y):
        pass

class mock_image_handler(object):

    def VideoCapture(self):
        return mock_camera()

class VideoCapture(object):

    def set(self, x, y):
        pass

def test_create_temp_photo_to_call_save_photo_and_store_path(mocker):
    controller = Controller(cam=mock_camera(), vision=mock_image_handler)
    controller.create_temp_photo()
    assert controller.photo_path == "a string"

def test_up_to_call_forward_and_store_photo(mocker):
    mocker.patch.object(car, 'forward')
    mock_cam = mock_camera()
    controller = Controller(cam=mock_cam, vision=mock_image_handler)
    controller.up()
    assert car.forward.called
    assert mock_cam.paths == ["current_image/test_string", "forward/test_string"]

def test_down_to_call_reverse_and_store_photo(mocker):
    mocker.patch.object(car, 'reverse')
    mock_cam = mock_camera()
    controller = Controller(cam=mock_cam, vision=mock_image_handler)
    controller.down()
    assert car.reverse.called
    assert mock_cam.paths == ["current_image/test_string", "reverse/test_string"]

def test_right_to_call_turn_right_and_store_photo(mocker):
    mocker.patch.object(car, 'turn_right')
    mock_cam = mock_camera()
    controller = Controller(cam=mock_cam, vision=mock_image_handler)
    controller.right()
    assert car.turn_right.called
    assert mock_cam.paths == ["current_image/test_string", "turn_right/test_string"]

def test_left_to_call_turn_left_and_store_photo(mocker):
    mocker.patch.object(car, 'turn_left')
    mock_cam = mock_camera()
    controller = Controller(cam=mock_cam, vision=mock_image_handler)
    controller.left()
    assert car.turn_left.called
    assert mock_cam.paths == ["current_image/test_string", "turn_left/test_string"]

def test_piv_right_to_call_pivot_right_and_store_photo(mocker):
    mocker.patch.object(car, 'pivot_right')
    mock_cam = mock_camera()
    controller = Controller(cam=mock_cam, vision=mock_image_handler)
    controller.piv_right()
    assert car.pivot_right.called
    assert mock_cam.paths == ["current_image/test_string", "pivot_right/test_string"]

def test_piv_left_to_call_pivot_left_and_store_photo(mocker):
    mocker.patch.object(car, 'pivot_left')
    mock_cam = mock_camera()
    controller = Controller(cam=mock_cam, vision=mock_image_handler)
    controller.piv_left()
    assert car.pivot_left.called
    assert mock_cam.paths == ["current_image/test_string", "pivot_left/test_string"]

def test_create_temp_photo_calls_camera_delete_current_photo():
    mock_cam = mock_camera()
    controller = Controller(cam=mock_cam, vision=mock_image_handler)
    controller.create_temp_photo()
    assert mock_cam.test_string == "deleted"

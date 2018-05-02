from controller import Controller
import mock
import pytest
from pytest_mock import mocker
import camera
import car

def test_create_temp_photo_to_call_save_photo(mocker):
    mocker.patch.object(camera, 'save_photo')
    Controller.create_temp_photo('')
    camera.save_photo.assert_called

def test_up_to_call_forward(mocker):
    mocker.patch.object(car, 'forward')
    controller = Controller()
    controller.up()
    car.forward.assert_called

def test_down_to_call_reverse(mocker):
    mocker.patch.object(car, 'reverse')
    controller = Controller()
    controller.down()
    car.reverse.assert_called

def test_right_to_call_turn_right(mocker):
    mocker.patch.object(car, 'turn_right')
    controller = Controller()
    controller.right()
    car.turn_right.assert_called

def test_left_to_call_turn_left(mocker):
    mocker.patch.object(car, 'turn_left')
    controller = Controller()
    controller.left()
    car.turn_left.assert_called

def test_piv_right_to_call_pivot_right(mocker):
    mocker.patch.object(car, 'pivot_right')
    controller = Controller()
    controller.piv_right()
    car.pivot_right.assert_called

def test_piv_left_to_call_pivot_left(mocker):
    mocker.patch.object(car, 'pivot_left')
    controller = Controller()
    controller.piv_left()
    car.pivot_left.assert_called

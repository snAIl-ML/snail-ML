from controller import Controller
import mock
import pytest
from pytest_mock import mocker
import camera
import car

def test_create_photo_to_call_save_photo(mocker):
    mocker.patch.object(camera, 'save_photo')
    Controller.create_photo('','forward')
    camera.save_photo.assert_called

def test_up_to_call_forward(mocker):
    mocker.patch.object(car, 'forward')
    # mocker.patch.object(Controller, '__init__')
    mocker.patch.object(Controller, 'create_photo')
    controller = Controller()
    controller.up()
    car.forward.assert_called

def test_down_to_call_reverse(mocker):
    mocker.patch.object(car, 'reverse')
    # mocker.patch.object(Controller, '__init__')
    mocker.patch.object(Controller, 'create_photo')
    controller = Controller()
    controller.down()
    car.reverse.assert_called

def test_right_to_call_turn_right(mocker):
    mocker.patch.object(car, 'turn_right')
    # mocker.patch.object(Controller, '__init__')
    mocker.patch.object(Controller, 'create_photo')
    controller = Controller()
    controller.right()
    car.turn_right.assert_called

def test_left_to_call_turn_left(mocker):
    mocker.patch.object(car, 'turn_left')
    # mocker.patch.object(Controller, '__init__')
    mocker.patch.object(Controller, 'create_photo')
    controller = Controller()
    controller.left()
    car.turn_left.assert_called

def test_piv_right_to_call_pivot_right(mocker):
    mocker.patch.object(car, 'pivot_right')
    # mocker.patch.object(Controller, '__init__')
    mocker.patch.object(Controller, 'create_photo')
    controller = Controller()
    controller.piv_right()
    car.pivot_right.assert_called

def test_piv_left_to_call_pivot_left(mocker):
    mocker.patch.object(car, 'pivot_left')
    # mocker.patch.object(Controller, '__init__')
    mocker.patch.object(Controller, 'create_photo')
    controller = Controller()
    controller.piv_left()
    car.pivot_left.assert_called

def test_take_extra_photo_to_call_create_photo(mocker):
    # mocker.patch.object(Controller, '__init__')
    mocker.patch.object(Controller, 'create_photo')
    controller = Controller()
    controller.take_extra_photo()
    Controller.create_photo.assert_called

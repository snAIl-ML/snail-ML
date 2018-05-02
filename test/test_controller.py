from controller import Controller
import mock
import pytest
from pytest_mock import mocker
import camera
import car

def test_create_temp_photo_to_call_save_photo(mocker):
    mocker.patch.object(camera, 'save_photo')
    Controller.create_temp_photo('')
    assert camera.save_photo.called

def test_up_to_call_forward_and_store_photo(mocker):
    mocker.patch.object(car, 'forward')
    mocker.patch.object(camera, 'move_photo')
    controller = Controller()
    controller.up()
    assert car.forward.called
    assert camera.move_photo.called

def test_down_to_call_reverse_and_store_photo(mocker):
    mocker.patch.object(car, 'reverse')
    controller = Controller()
    controller.down()
    assert car.reverse.called

def test_right_to_call_turn_right_and_store_photo(mocker):
    mocker.patch.object(car, 'turn_right')
    controller = Controller()
    controller.right()
    assert car.turn_right.called

def test_left_to_call_turn_left_and_store_photo(mocker):
    mocker.patch.object(car, 'turn_left')
    controller = Controller()
    controller.left()
    assert car.turn_left.called

def test_piv_right_to_call_pivot_right_and_store_photo(mocker):
    mocker.patch.object(car, 'pivot_right')
    controller = Controller()
    controller.piv_right()
    assert car.pivot_right.called

def test_piv_left_to_call_pivot_left_and_store_photo(mocker):
    mocker.patch.object(car, 'pivot_left')
    controller = Controller()
    controller.piv_left()
    assert car.pivot_left.called

import path_helper_test_main
import pytest
from pytest_mock import mocker
from snail import *
from controller import Controller

# mock functions
def mock_AI_func(args):
    pass

def mock_user_supervisor_func():
    pass

# tests
def test_AI_loop_calls_create_temp_photo(mocker):
    mocker.patch.object(Controller, 'create_temp_photo')
    AI_loop(counter=1, ai=mock_AI_func, user=mock_user_supervisor_func)
    assert Controller.create_temp_photo.called

def test_AI_loop_calls_AI_function():
    # something involving mock_AI_func
    pass

def test_AI_loop_calls_user_supervision_func_after_counter_reaches_target():
    pass

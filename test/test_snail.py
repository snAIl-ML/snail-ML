'Test'
# check unused imports
import pytest
from pytest_mock import mocker
import path_helper_test_main
from snail import *

class mock_Controller(object):
    'Class'

    def create_temp_photo(self):
        'Function'
        pass

    def up(self):
        'Function'
        pass

    def down(self):
        'Function'
        pass

    def piv_right(self):
        'Function'
        pass

    def piv_left(self):
        'Function'
        pass

    def clear_current_image_folder(self):
        'Function'
        pass


# mock functions
def mock_ai_func():
    'Function'
    return 'forward'

def mock_user_supervisor_func():
    'Function'
    return "I am being called"

def mock_image_path():
    'Function'
    return 'an image path'

# tests
def test_ai_loop(mocker):
    'test_ai_loop_calls_create_temp_photo'
    mocker.patch.object(mock_Controller, 'create_temp_photo')
    ai_loop(counter=0, ai=mock_ai_func, user=mock_user_supervisor_func, control=mock_Controller)
    assert mock_Controller.create_temp_photo.called

def test_ai_loop_also(mocker):
    'test_ai_loop_calls_ai_function_and_applies_motion'
    mocker.patch.object(mock_Controller, 'create_temp_photo')
    mocker.patch.object(mock_Controller, 'up')
    ai_loop(counter=1,
            ai=mock_ai_func,
            user=mock_user_supervisor_func,
            img_path=mock_image_path,
            control=mock_Controller)
    assert mock_Controller.up.called

def test_ai_loop_as_well(mocker):
    'test_ai_loop_calls_user_supervision_func_after_counter_reaches_target'
    assert (ai_loop(counter=0,
                    ai=mock_ai_func,
                    user=mock_user_supervisor_func,
                    img_path=mock_image_path,
                    control=mock_Controller)
           ) == "I am being called"

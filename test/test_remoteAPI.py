import path_helper_test_main
from remoteAPI import *


def test_index_route_initializes_photo_loop_and_asks_for_photo_path(mocker):
    tester = app.test_client()
    mocker.patch.object(controller, 'create_temp_photo')
    mocker.patch.object(controller, 'get_photoname')
    response = tester.get('/', content_type='html/text')
    assert (response.status_code) == 200
    assert (controller.create_temp_photo.called)
    assert (controller.get_photoname.called)

def test_FEATURE_index_route_captures_and_renders_photo_path(mocker):
    tester = app.test_client()
    response = tester.get('/', content_type='html/text')
    assert (response.status_code) == 200
    assert('img src=' in response.data.decode("utf8"))

def test_forward_route_calls_up_function_and_redirects_to_index(mocker):
    tester = app.test_client()
    mocker.patch.object(controller, 'up')
    mocker.patch.object(controller, 'create_temp_photo')
    mocker.patch.object(controller, 'get_photoname')
    response = tester.get('/forward', content_type='html/text', follow_redirects=True)
    assert (response.status_code) == 200
    assert (controller.up.called)
    assert (controller.create_temp_photo.called)
    assert (controller.get_photoname.called)

def test_pivot_left_route_calls_pivot_left_function_and_redirects_to_index(mocker):
    tester = app.test_client()
    mocker.patch.object(controller, 'piv_left')
    mocker.patch.object(controller, 'create_temp_photo')
    mocker.patch.object(controller, 'get_photoname')
    response = tester.get('/piv_left', content_type='html/text', follow_redirects=True)
    assert (response.status_code) == 200
    assert (controller.piv_left.called)
    assert (controller.create_temp_photo.called)
    assert (controller.get_photoname.called)

def test_pivot_right_route_calls_pivot_right_function_and_redirects_to_index(mocker):
    tester = app.test_client()
    mocker.patch.object(controller, 'piv_right')
    mocker.patch.object(controller, 'create_temp_photo')
    mocker.patch.object(controller, 'get_photoname')
    response = tester.get('/piv_right', content_type='html/text', follow_redirects=True)
    assert (response.status_code) == 200
    assert (controller.piv_right.called)
    assert (controller.create_temp_photo.called)
    assert (controller.get_photoname.called)

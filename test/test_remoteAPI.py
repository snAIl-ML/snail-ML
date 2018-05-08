import path_helper_test_main
from remoteAPI import *


def test_index_route_initializes_photo_loop(mocker):
    tester = app.test_client()
    mocker.patch.object(controller, 'create_temp_photo')
    response = tester.get('/', content_type='html/text')
    assert (response.status_code) == 200
    assert ('snail remote control API' in response.data.decode("utf8"))
    assert (controller.create_temp_photo.called)

def test_forward_route_calls_up_function(mocker):
    tester = app.test_client()
    mocker.patch.object(controller, 'up')
    response = tester.get('/forward', content_type='html/test')
    assert (response.status_code) == 200
    assert ('forward' in response.data.decode("utf8"))
    assert (controller.up.called)

def test_pivot_left_route_calls_pivot_left_function(mocker):
    tester = app.test_client()
    mocker.patch.object(controller, 'piv_left')
    response = tester.get('/piv_left', content_type='html/test')
    assert (response.status_code) == 200
    assert ('piv_left' in response.data.decode("utf8"))
    assert (controller.piv_left.called)

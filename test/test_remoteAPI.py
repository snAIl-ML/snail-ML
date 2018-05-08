import path_helper_test_main
from remoteAPI import *


def test_index_route():
    tester = app.test_client()
    response = tester.get('/', content_type='html/text')
    assert (response.status_code) == 200
    assert ('snail remote control API' in response.data.decode("utf8"))

def test_forward_route(mocker):
    tester = app.test_client()
    mocker.patch.object(controller, 'up')
    response = tester.get('/forward', content_type='html/test')
    assert (response.status_code) == 200
    assert ('forward' in response.data.decode("utf8"))
    assert (controller.up.called)

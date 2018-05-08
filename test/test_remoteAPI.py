import path_helper_test_main
from remoteAPI import app

def test_index_page():
    tester = app.test_client()
    response = tester.get('/', content_type='html/text')
    assert (response.status_code) == 200
    assert ('snail remote control API' in response.data.decode("utf8"))

import os

def get_server_move(image_path, url):
    server_move = requests.post(url, files = {'image': open(image_path, 'rb')})
    return server_move.text

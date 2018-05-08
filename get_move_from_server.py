'Module to get response from the server'
import requests

def get_server_move(image_path, url):
    'Function to get response from the server'
    server_move = requests.post(url, files={'image': open(image_path, 'rb')})
    return server_move.text

'Module to get response from the server'
import requests

def get_server_move(image_path, url):
    print('Function to get response from the server')
    print(url)
    print(image_path)
    # print({'image': open(image_path, 'rb')})
    server_move = requests.post(url, files={'image': open(image_path, 'rb')})
    print(server_move.text)
    return server_move.text

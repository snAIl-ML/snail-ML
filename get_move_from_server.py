'Module to get response from the server'
import os

def get_server_move(image_path, url):
    'Function to get response from the server'
    #nb this is acknowledged as terrible, terrible code
    response_file = "response.txt"
    post_command = ("curl -o response.txt -F 'image=@" +
                    image_path + "' " + url)
    os.system(post_command)
    output = ""
    with open(response_file) as file:
        for line in file:
            output = output + line
    with open(response_file, 'w'): pass
    return output

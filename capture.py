from datetime import datetime
import time
import cv2
import os
# imports openCV for usage

def TakePicture(action):
    # create image directory if doesn't exist already
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/images/' + action
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # creates an object called camera, of type openCV video capture, using the first camrea in the list of cameras connected to the computer.
    camera = cv2.VideoCapture(0)

    img = ''
    # loop to take 5 photos
    for i in range(5):
        # sleep for a second between every photo
        time.sleep(1)

        # read values from the camera object, using it's read method.
        # it resonds with 2 values save the 2 data values into two temporary
        # variables called "return_value" and "image"
        return_value, image = camera.read()

        img_name = dir_path + '/' + str(datetime.now().strftime('%Y-%m-%d %H-%M-%S')) + '.png'
        cv2.imwrite(img_name, image)
    # use the openCV method imwrite (that writes an image to a disk) and write an image using the data in the temporary data variable
        print(img_name)

    # deletes the camrea object, also releases camera
    del(camera)


TakePicture('reverse')

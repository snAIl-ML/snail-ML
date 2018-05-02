import turtle
import car as car
import camera

class Controller(object):

    def __init__(self, car=car, cam=camera):
        self.cam = cam
        self.photo_path = "replace me"
        self.car = car
        turtle.setup(400,500)
        self.window = turtle.Screen()
        self.window.title('snAIl Controller')
        self.window.bgcolor('blue')

    def create_temp_photo(self):
        img_data = self.cam.grab_image_data()
        dir_path = self.cam.create_path("temp")
        self.cam.create_directory(dir_path)
        self.photo_path = self.cam.save_photo(dir_path, img_data)

    def up(self):
        new_path = self.cam.create_path("forward")
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path)
        self.car.forward(0.2)

    def down(self):
        new_path = self.cam.create_path("reverse")
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path)
        self.car.reverse(0.2)

    def right(self):
        self.car.turn_right(0.2)

    def left(self):
        self.car.turn_left(0.2)

    def piv_right(self):
        self.car.pivot_right(0.2)

    def piv_left(self):
        self.car.pivot_left(0.2)

    def exit(self):
        self.window.bye()

def main():
    w = Controller()
    w.window.onkey(w.up, 'Up')
    w.window.onkey(w.down, 'Down')
    w.window.onkey(w.right, 'Right')
    w.window.onkey(w.left, 'Left')
    w.window.onkey(w.piv_right, '/')
    w.window.onkey(w.piv_left, '.')
    w.window.onkey(w.exit, 'q')
    w.window.listen()
    w.window.mainloop()

    pass

if __name__ == "__main__":
   main()

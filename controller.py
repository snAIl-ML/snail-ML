import turtle
import car as car
import camera

class Controller(object):

    def __init__(self, car = car):
        self.car = car
        turtle.setup(400,500)
        self.window = turtle.Screen()
        self.window.title('snAIl Controller')
        self.window.bgcolor('blue')

    def create_photo(self, action):
        img_data = camera.grab_image_data()
        dir_path = camera.create_path(action)
        camera.create_directory(dir_path)
        camera.save_photo(dir_path, img_data)

    def up(self):
        self.create_photo('forward')
        self.car.forward(0.2)

    def down(self):
        self.create_photo('reverse')
        self.car.reverse(0.2)

    def right(self):
        self.create_photo('turn_right')
        self.car.turn_right(0.2)

    def left(self):
        self.create_photo('turn left')
        self.car.turn_left(0.2)

    def piv_right(self):
        self.create_photo('pivot_right')
        self.car.pivot_right(0.2)

    def piv_left(self):
        self.create_photo('pivot_left')
        self.car.pivot_left(0.2)

    def take_extra_photo(self):
        print('Taking extra photo')
        self.create_photo('extra')

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
    w.window.onkey(w.take_extra_photo, 'p')
    w.window.onkey(w.exit, 'q')
    w.window.listen()
    w.window.mainloop()

    pass

if __name__ == "__main__":
   main()

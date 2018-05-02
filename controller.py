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
        dir_path = self.cam.create_path("current_image")
        self.cam.create_directory(dir_path)
        self.photo_path = self.cam.save_photo(dir_path, img_data)

    def up(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("forward")
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.forward(0.2)
        self.create_temp_photo()

    def down(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("reverse")
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.reverse(0.2)
        self.create_temp_photo()

    def right(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("turn_right")
        self.cam.create_directory(new_path)
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.turn_right(0.2)
        self.create_temp_photo()

    def left(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("turn_left")
        self.cam.create_directory(new_path)
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.turn_left(0.2)
        self.create_temp_photo()

    def piv_right(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("pivot_right")
        self.cam.create_directory(new_path)
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.pivot_right(0.2)
        self.create_temp_photo()

    def piv_left(self):
        photoname = self.photo_path.split("/")[-1]
        new_path = self.cam.create_path("pivot_left")
        self.cam.create_directory(new_path)
        self.cam.create_directory(new_path)
        self.cam.move_photo(self.photo_path, new_path + "/" + photoname)
        self.car.pivot_left(0.2)
        self.create_temp_photo()

    def exit(self):
        self.window.bye()

def main():
    w = Controller()
    w.create_temp_photo()
    w.window.onkey(w.up, 'Up')
    w.window.onkey(w.down, 'Down')
    w.window.onkey(w.right, 'Right')
    w.window.onkey(w.left, 'Left')
    w.window.onkey(w.piv_right, '/')
    w.window.onkey(w.piv_left, '.')
    w.window.onkey(w.exit, 'q')
    w.window.listen()
    w.window.mainloop()

if __name__ == "__main__":
   main()

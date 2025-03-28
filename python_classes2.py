
class Cylinder:

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height


    def draw(self):
        result = ( 22/7* self.radius ** 2 * 2 + 2 * 22/7 * self.radius * self.height)
        print(f"Area is: {result}")

    def volume(self):
        result = ( 22/7 * self.radius ** 2 * 2 * self.height)
        print(f"Volume is: {result}")

    def print_details(self):
        print(f"Radius is: {self.radius}" and f"Height is: {self.height}")
from math import pi

class Cylinder:

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return pi * (self.radius ** 2) * self.height


    def surface_area(self):
        top = pi * self.radius ** 2
        return (2 * top) + (2 * pi * self.radius * self.height)


c = Cylinder(height=2, radius=3)
v_result = c.volume()
area_result = c.surface_area()
print(f'{v_result:.2f}')
print(f'{area_result:.2f}')


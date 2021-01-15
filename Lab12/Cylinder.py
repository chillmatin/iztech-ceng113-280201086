class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def set_radius(self, radius):
        self.radius = radius
    
    def set_height(self, height):
        self.height = height
    
    def get_radius(self):
        return self.radius
    
    def get_height(self):
        return self.height
        
    def volume(self):
        return self.radius ** 2 * self.height
    
    def area(self):
        return self.radius ** 2 * 3.14 + self.radius * 3.14 * 2 * self.height

instance = Cylinder(3, 5)
print(instance.get_height())
print(instance.area())
print(instance.volume())
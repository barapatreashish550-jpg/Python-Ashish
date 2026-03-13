import math

class Polar:
    def __init__(self, r, a):
        self.r = r        # radius
        self.a = a        # angle in radians

    def __add__(self, other):
        
        x1 = self.r * math.cos(self.a)
        y1 = self.r * math.sin(self.a)

        x2 = other.r * math.cos(other.a)
        y2 = other.r * math.sin(other.a)

        
        x = x1 + x2
        y = y1 + y2

        
        r = math.sqrt(x*x + y*y)
        a = math.atan2(y, x)

        return Polar(r, a)

    def display(self):
        print("Radius:", self.r)
        print("Angle (radians):", self.a)


p1 = Polar(5, 0.5)
p2 = Polar(4, 1.0)

p3 = p1 + p2

print("Resultant Polar Coordinates:")
p3.display()
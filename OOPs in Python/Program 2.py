
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print("Max Speed:", self.max_speed)
        print("Mileage:", self.mileage)

class Bus(Vehicle):
    pass   

bus1 = Bus(120, 10)

bus1.display()
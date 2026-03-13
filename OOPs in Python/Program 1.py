class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# creating object
car = Vehicle(180, 25)

# printing values
print("Max Speed:", car.max_speed)
print("Mileage:", car.mileage)
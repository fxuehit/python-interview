class Vehicle:
    def __init__(self, numberOfWheel=2):
        self.wheels = numberOfWheel

    def horn(self):
        print("This is a vehicle")

    def howmanyWheel(self):
        return self.wheels


class Car(Vehicle):
    def __init__(self, numberOfWheel):
        super().__init__(numberOfWheel)
        #self.wheels = 4

    def horn(self):
        print("This is a car")


class Truck(Vehicle):
    def __init__(self, numberOfWheel):
        super().__init__(numberOfWheel)
        #self.wheels = 6

    def horn(self):
        print("This is a truck")


# Create an object of the Car class
my_car = Car(4)
print("Number of wheels in the car:", my_car.howmanyWheel())
my_car.horn()

# Create an object of the Truck class
my_truck = Truck(100)
print("Number of wheels in the truck:", my_truck.howmanyWheel())
my_truck.horn()

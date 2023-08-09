from abc import ABC, abstractproperty

class Vehicle(ABC):
    @abstractproperty
    def wheels(self):
        pass

    @abstractproperty
    def max_speed(self):
        pass

class Car(Vehicle):
    wheels = 4
    max_speed = 200

class Bicycle(Vehicle):
    wheels = 2
    max_speed = 30

car = Car()
bicycle = Bicycle()

print(car.wheels)        # Output: 4
print(car.max_speed)     # Output: 200
print(bicycle.wheels)    # Output: 2
print(bicycle.max_speed) # Output: 30

from random import randint
from prac_09.car import Car
class UnreliableCar(Car):
    """  """
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_chance = randint(0, 100)#random number ranging from 0 to 100

        if random_chance < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0

        return distance_driven # only drive if the random number is less than the car's reliability
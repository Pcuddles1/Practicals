
from Prac_08.car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliability_test = random.randint(0,100)
        print(self.reliability, reliability_test)
        if reliability_test > self.reliability:
            super().drive(distance)
        return distance
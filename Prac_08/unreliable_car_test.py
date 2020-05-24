from Prac_08.unreliable_car import UnreliableCar
import random

def main():
    car = UnreliableCar(100,"bCar", 60)
    print("{} {} {}".format(car.name, car.fuel, car.reliability))
    car.drive(20)
    print(car.odometer, car.fuel)




main()
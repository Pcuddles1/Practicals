from Prac_08.taxi import Taxi


def main():
    Prius = Taxi(100, "prius 1")
    print(Prius.fuel)
    Prius.drive(40)
    print("Name: {}\nOdometer: {}\nFuel: {}\nDistance: {}\nFare: {}".format(Prius.name, Prius.odometer, Prius.fuel,
                                                                            Prius.current_fare_distance,
                                                                            Prius.get_fare()))
    Prius.start_fare()
    Prius.drive(100)
    print("\nName: {}\nOdometer: {}\nFuel: {}\nDistance: {}\nFare: {}".format(Prius.name, Prius.odometer, Prius.fuel,
                                                                              Prius.current_fare_distance,
                                                                              Prius.get_fare()))


main()

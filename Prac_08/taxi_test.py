from Prac_08.taxi import Taxi


def main():
    Prius = Taxi(100, "prius 1")
    Prius.drive(40)
    print(Prius,"\n$",Prius.get_fare())
    Prius.start_fare()
    Prius.drive(100)
    print(Prius,"\n$",Prius.get_fare())


main()

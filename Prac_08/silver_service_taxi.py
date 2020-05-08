from Prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
    def get_fare(self):
        fare = super().get_fare()
        fare = (fare*self.fanciness)
        return fare
    def __str__(self):
        return "{}, total of=${}".format(super().__str__(), self.get_fare())
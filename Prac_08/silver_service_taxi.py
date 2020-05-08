from Prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.5
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
    def get_fare(self):
        fare = super().get_fare()
        fare = (fare*self.fanciness)+self.flagfall
        return fare
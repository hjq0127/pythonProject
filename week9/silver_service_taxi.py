"""
CP1404/CP5632 Practical
SilverServiceTaxi class, derived from Taxi
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel,)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} on current fare,plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return self.flagfall + super().get_fare()

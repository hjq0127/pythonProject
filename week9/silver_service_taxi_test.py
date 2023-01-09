"""
CP1404/CP5632 Practical -
SilverServiceTaxi class tests
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    taxi.drive(0)
    print(taxi)
    print(taxi.get_fare(), "$")


main()

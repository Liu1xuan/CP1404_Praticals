"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from Prac_06 import car


def main():
    """Demo test code to show how to use car class."""
    my_car = car.Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = car.Car(100)
    limo.add_fuel(20)
    print(f"Fuel amount in the car:{limo.fuel} liters")

    distance_drive = limo.drive(115)
    print(f"Distance_driven:{distance_drive} km")

    print(limo)


main()

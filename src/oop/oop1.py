# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle():
    # base class - lvl 1
    pass


# FLIGHT VEHICLES #
class FlightVehicle(Vehicle):
    # sub class - lvl 2
    pass


class Starship(FlightVehicle):
    # sub class - lvl 3
    pass


class Airplane(FlightVehicle):
    # sub class - lvl 3
    pass


# GROUND VEHICLES
class GroundVehicle(Vehicle):
    # sub class - lvl 2
    pass


class Car(GroundVehicle):
    # sub class - lvl 3
    pass


class Motorcycle(GroundVehicle):
    # sub class - lvl 3
    pass

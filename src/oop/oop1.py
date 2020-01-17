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

# Base Class Vehicle


class Vehicle:
    pass


# GroundVehicle extends Vehicle

class GroundVehicle(Vehicle):
    pass

# Car and Motorcycle inherit from GroundVehicle


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass


# FlightVehicle extends Vehicle

class FlightVehicle(Vehicle):
    pass

# Starship and Airplane inherit from FlightVehicle


class Starship(FlightVehicle):
    pass


class Airplane(FlightVehicle):
    pass

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

# Base class
class Vehicle: 
    pass
# Base class for ground vehicles
class GroundVehicle(Vehicle):
    pass
# child class of ground vehicles
class Car(GroundVehicle):
    pass
# child class of ground vehicles
class Motorcycle(GroundVehicle):
    pass
# Base calss for flight vehicles
class FlightVehicle(Vehicle):
    pass
# child class of flight vehicles
class Starship(FlightVehicle):
    pass
# child class of flight vehicles
class Airplane(FlightVehicle):
    pass
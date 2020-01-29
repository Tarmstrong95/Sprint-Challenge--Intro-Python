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
class Vehicle:
	"""Base class"""
	pass
class FlightVehicle(Vehicle):
	"""lvl-2 class"""
	pass
class Starship(FlightVehicle):
	"""lvl-3 class"""
	pass
class Airplane(FlightVehicle):
	"""lvl-3 class"""
	pass
class GroundVehicle(Vehicle):
	"""lvl-2 class"""
	pass
class Car(GroundVehicle):
	"""lvl-3 class"""
	pass
class Motorcycle(GroundVehicle):
	"""lvl-3 class"""
	pass

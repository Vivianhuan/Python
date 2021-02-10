#Chapter 9 Inheritance
# The __init__() Method for a Child Class
class Car:
	"""A simple attempt to repreent a car. """
	def __init__(self, make, model, year):
		"""Initialize attributes to a car."""
		self.make = make
		self.model= model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return all information we know about a car."""
		long_name= f"{self.make} {self.model} {self.year}"	
		return long_name.title()
	def update_odometer(self,mileage):
		"""Update odometer mileage to an attribute of a car."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer.")
	def read_odometer(self):
		"""Display odometer about a car."""
		print(f"This car has {self.odometer_reading} miles on it.")
	def increment_odometer(self,miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

class ElecticCar(Car):
	"""Represent aspects of a car, specific to eletric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model,year)
my_tesla = ElecticCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())

#Defining Attributes and Methods for the Child Class
#Let’s add an attribute that’s specific to electric cars 
#(a battery, for example) and a method to report on this attribute. 
#We’ll store the battery size and write a method that prints a 
#escription of the battery. 

class Car:
	"""A simple attempt to repreent a car. """
	def __init__(self, make, model, year):
		"""Initialize attributes to a car."""
		self.make = make
		self.model= model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return all information we know about a car."""
		long_name= f"{self.make} {self.model} {self.year}"	
		return long_name.title()
	def update_odometer(self,mileage):
		"""Update odometer mileage to an attribute of a car."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer.")
	def read_odometer(self):
		"""Display odometer about a car."""
		print(f"This car has {self.odometer_reading} miles on it.")
	def increment_odometer(self,miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

class ElecticCar(Car):	
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class.
		Then initiliaze specific attribute to electric cars."""
		super().__init__(make, model,year)
		self.battery_size = 75
	def describe_battery(self):
		"""Print a statement that describes the battery size of electric car."""
		print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla = ElecticCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())	
my_tesla.describe_battery()		

#Break large class into smaller classes
class Car:
	"""A simple attempt to repreent a car. """
	def __init__(self, make, model, year):
		"""Initialize attributes to a car."""
		self.make = make
		self.model= model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return all information we know about a car."""
		long_name= f"{self.make} {self.model} {self.year}"	
		return long_name.title()
	def update_odometer(self,mileage):
		"""Update odometer mileage to an attribute of a car."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer.")
	def read_odometer(self):
		"""Display odometer about a car."""
		print(f"This car has {self.odometer_reading} miles on it.")
	def increment_odometer(self,miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
class Battery:
	"""A simple attempt to model a battery for a electric car."""
	def __init__(self, battery_size = 75):
		"""Initialize the battery's attribute."""
		self.battery_size = battery_size
	def describe_battery(self):
		"""Display a statement that describes the battery's attributes."""
		print(f"This car has a {self.battery_size}-kwh battery.")
class ElecticCar(Car):
	"""Represent aspects of a car, specific to electric cars."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class.
		Then initialize new attribute specific to electric car."""
		super().__init__(make,model,year)
		self.battery = Battery()	
my_tesla = ElecticCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()

# Practice 9-6
class Restaurant:
	"""A class representing a restaurant."""
	def __init__(self,restaurant_name,cuisine_type):
		"""Initialize the name and cuisine type attributes to a restarant."""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		"""Display restaurant's name and cuisine type."""
		print(f"The restaurant's name is {self.restaurant_name}. It serves wonderful {self.cuisine_type}.")

class Flavors:
	"""Represent all flavors to the specific restaurant."""
	def __init__(self,icecream_flavor = 'strawberry'):
		"""Initialize attribute to ice cream stands."""
		self.icecream_flavor = icecream_flavor
	def show_flavors(self):
		"""Show statement about the ice cream's flavor."""
		print(f"Your ice cream is {self.icecream_flavor} of flavor. Enjoy it!")

class IceCreamStand(Restaurant):
	"""Represent all aspects of a restaurant, specific to an ince cream stand."""
	def __init__(self,restaurant_name,cuisine_type):
		"""Initialize attributes of parent class
		Then initialize new attribute specific to ice cream."""
		super().__init__(restaurant_name,cuisine_type)
		self.flavor = Flavors()

my_icecream = IceCreamStand('blue bell','ice creams')
my_icecream.describe_restaurant()

my_icecream.flavor.show_flavors()














############Chapter 9
############
#Working with Classes and Instances
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self,make,model,year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.model} {self.make}"
		return long_name.title()
my_new_car = Car('audi','a6','2020')
print(my_new_car.get_descriptive_name())

#To make the class more interesting, let’s add an attribute 
#that changes over time. We’ll add an attribute that stores the 
#car’s overall mileage.
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return neatly formatted information about a car."""
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()
	def read_odometer(self):
		"""Printing a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")	
my_new_car = Car('audi','a6',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Not many cars are sold with exactly 0 miles on the odometer, 
#so we need a way to change the value of this attribute.
#There are 3 ways to modify an attribute:
#1st:
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return neatly formatted information about a car."""
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()
	def read_odometer(self):
		"""Printing a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")	
my_new_car = Car('audi','a6',2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()			

#2nd:Modifying an Attribute's Value Through a Method
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return neatly formatted information about a car."""
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()
	def update_odometer(self,mileage):
		"""Set the odometer reading to the given value."""
		self.odometer_reading = mileage
	def read_odometer(self):
		"""Printing a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")	
	
my_new_car = Car('audi','a6',2020)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()	

#We can extend the method update_odometer() to do additional work
#every time the odometer reading is modified. Let’s add a little 
#logic to make sure no one tries to roll back the odometer reading:
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return neatly formatted information about a car."""
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()
	def update_odometer(self,mileage):
		"""Set the odometer reading to the given value."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")	
	def read_odometer(self):
		"""Printing a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi','a6',2020)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()	

my_new_car.update_odometer(20)
my_new_car.read_odometer()

#3rd:
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
my_new_car = Car('audi','a6',2020)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(20)
my_new_car.read_odometer()

#Practice 9-4
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
	def read_number_served(self):
		"""Display the total number people served at the restarant."""
		print(f"The restaurant has served {self.number_served} customers.")	
	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		print(f"{self.restaurant_name} is open. Come on in!")	

restaurant= Restaurant('pizza hut','pizza')
restaurant.describe_restaurant()
restaurant.number_served =27
restaurant.read_number_served()
restaurant.open_restaurant()

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
	def set_number_served(self,customer_number):
		"""Given new value to the class."""
		if customer_number >= self.number_served:
			self.number_served = customer_number
		else:
			print("You can't roll back the number of people served!")
	def read_number_served(self):
		"""Display the total number people served at the restarant."""
		print(f"The restaurant has served {self.number_served} customers.")	
	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		print(f"{self.restaurant_name} is open. Come on in!")	

restaurant= Restaurant('pizza hut','pizza')
restaurant.describe_restaurant()

restaurant.set_number_served(30)
restaurant.read_number_served()

restaurant.set_number_served(25)
restaurant.read_number_served()

restaurant.open_restaurant()


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
	def set_number_served(self,customer_number):
		"""Given new value to the class."""
		if customer_number >= self.number_served:
			self.number_served = customer_number
		else:
			print("You can't roll back the number of people served!")
	def increment_number_served(self,number):
		"""Add given number to the value."""
		self.number_served += number
	def read_number_served(self):
		"""Display the total number people served at the restarant."""
		print(f"The restaurant has served {self.number_served} customers.")	
	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		print(f"{self.restaurant_name} is open. Come on in!")	


restaurant= Restaurant('pizza hut','pizza')
restaurant.describe_restaurant()

restaurant.set_number_served(30)
restaurant.read_number_served()

restaurant.increment_number_served(15)
restaurant.read_number_served()

restaurant.increment_number_served(5)
restaurant.read_number_served()

restaurant.set_number_served(21)
restaurant.read_number_served()

restaurant.open_restaurant()

#Pratice 9-5
class User:
	"""A simple attempt to represent a user."""
	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize attributes to a user."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()
		self.login_attempts = 0
	def describe_user(self):
		"""Display a summary of a user."""
		print(f"{self.first_name} {self.last_name}")
		print("		Username: {self.username}")	
		print("		Email: {self.email}")	
		print("		Location: {self.location}")	
	def set_login_attempts(self,number_attempts):
		"""Set up new value to a user."""
		if number_attempts >= self.login_attempts:
			self.login_attempts = number_attempts
		else:
			print("You can't roll back the number of login attempts!")	
	def increment_login_attempts(self,attempt = 1):
		"""Add given number to the value."""
		self.login_attempts += attempt
	def read_attempts(self):
		"""Display the number of login attempts about a user."""
		print(f"This user has logged in {self.login_attempts} times.")	
	def reset_login_attempts(self):
		"""Reset the value to 0."""
		self.login_attempts = 0
	def greet_user(self):
		"""Display a simple greeting to a user."""
		print(f"Welcome back, {self.username}!")
		
user1= User('alice','lee','a_lee','alie@gmail.com','california')
user1.describe_user()
user1.greet_user()

user1.set_login_attempts(5)
user1.read_attempts()

user1.increment_login_attempts()
user1.read_attempts()

user1.increment_login_attempts()
user1.read_attempts()

user1.reset_login_attempts()
user1.increment_login_attempts()
user1.read_attempts()
















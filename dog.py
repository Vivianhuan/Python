############Chapter 9
############Creating and Using a Class
#Creating the dog class
class Dog:
	"""A simple attempt to model a dog."""
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")	
	def roll_over(self):
		"""Simulate a dog rolling over in response to a command."""
		print(f"{self.name} is now rolling over.")	

############
#Making an Instance from a Class
my_dog = Dog('willie',6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

#############
#Calling Methods
my_dog.sit()
my_dog.roll_over()

##############
#Creating Multiple Instances
my_dog = Dog('willie',6)
print(f"My dog's name is {my_dog.name}.And she is {my_dog.age} years old.")
my_dog.sit()


your_dog = Dog('Lucy',3)
print(f"My dog's name is {your_dog.name}.And she is {your_dog.age} years old.")
your_dog.sit()

#Practice 9-1
class Restaurant:
	"""A class representing a restaurant."""
	def __init__(self,restaurant_name,cuisine_type):
		"""Initialize the name and cuisine type attributes to a restarant."""
		self.name = restaurant_name.title()
		self.type = cuisine_type
	def describe_restaurant(self):
		"""Display restaurant's name and cuisine type."""
		print(f"The restaurant's name is {self.name}. It serves wonderful {self.type}.")

	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		print(f"{self.name} is open. Come on in!")	
restaurant= Restaurant('pizza hut','pizza')
print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#Practice 9-2
restaurant1 = Restaurant('pho corner','Vietnamese foods')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('Sushi Sake','sushi')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('taco bell','tacos')
restaurant3.describe_restaurant()

#Practice 9-3
class User:
	"""Set up a class of user profile."""
	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize first and last name to a user."""
		self.first = first_name.title()
		self.last = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()
	def describe_user(self):	
		"""Summary of information about a user."""
		print(f"{self.first} {self.last}")
		print(f"	username: {self.username}")
		print(f"	email: {self.email}")
		print(f"	Location: {self.location}")
	def greet_user(self):
		"""Display a simple greeting sentence to a user. """
		print(f"Welcome back, {self.username}! ")	
user1 = User('eric','matthes','e_matthes','e_matthes@example.com','alaska')
user1.describe_user()
user1.greet_user()

user2 = User('alice','lee','a_lee','alie@yahoo.com','california')
user2.describe_user()
user2.greet_user()		














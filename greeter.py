# Difining a function
def greeter_user():
	"""Display a simple greeting."""
	print("Hello!")

greeter_user()

#Paasing information to a function
def greeter_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")	

greeter_user('vivian')

# Practice 8-1
def display_message():
	"""Display what I have learned from Chapter 8."""
	print("Until now I have learned how to define a function in Python and how to pass the information to the function.")

display_message()

# Passing arguments: positional arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type.title()}.")
	print(f"My pet's name is {pet_name.title()}.")
describe_pet('labradoodle','daqian zheng')


# Passing arguments: keyword arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type.title()}.")
	print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'hamster',pet_name = 'harry')
describe_pet(pet_name = 'harry',animal_type = 'hamster')

# Passing arguments: default values
def describe_pet(pet_name,animal_type='dog'):
	"""Display information about a dog."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('willie')
## To describe an animal other than a dog, you could use a function call 
## Because an explicit argument for animal_type is provided, Python will
## ignore the parameter’s default value.
describe_pet('Daqian Zheng','labradoodle')

# Practice 8-3
def make_shirt(size,message):
	"""Display size information about a t-shirt"""
	print(f"\nI am going to make a {size} shirt.")
	print(f'It will say "{message}".')

make_shirt('small', 'I like running!')

# Practice 8-4
def make_shirt(message = 'I love Python!',size = 'large'):
	"""Display texts on shirts."""
	print(f"\nI am going to make a {size} shirt.")
	print(f'It will say "{message}".')
make_shirt()
make_shirt(size = 'medium')
make_shirt(size = 'small', message = 'I like Beijing!')

# Practice 8-5
def describe_city(name,country = 'China'):
	"""Display the country of the city."""
	print(f"\n{name.title()} is in {country}.")
describe_city('shanghai')	
describe_city('shenzhen')
describe_city('new york', 'United States')

# Returning a simple value to simplify the codes
def get_formatted_name(first_name,last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

# Making an argument optional
def get_formatted_name(first_name,middle_name,last_name):
	"""Display a full name, neatly formatted."""
	full_name=f"{first_name} {middle_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
	"""Display the full name, neatly formatted."""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"	
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)	

musician = get_formatted_name('john','hooker','lee')
print(musician)	

# Returning a dictionary
def build_person(first_name,last_name):
	"""Return a dictionary of information about a person."""
	person = {'first':first_name,'last':last_name}
	return person
musician = build_person('jimi','hendrix')
print(musician)	

def build_person(first_name,last_name,age=None):
	"""Return a dictionaey of information about a person."""
	person = {'first':first_name,'last':last_name}
	if age:
		person['age']= age
	return person
musician = build_person('jimi','hendrix',age = 27)
print(musician)		
musician = build_person('jimi','hendrix')
print(musician)

# Using a function with a while loop: guess it may need to refer to Terminal

#def get_formatted_name(first_name, last_name):
#	"""Return a full name, neatly formatted."""
#	full_name = f"{first_name} {last_name}"
#	return full_name.title()

#while True:
#	print("\nPlease tell me your name:")
#	print("(enter 'q' at any time to quit)")
#	f_name = input("First name:")
#	if f_name == 'q':
#		break
#	l_name = input("Last name:")
#	if l_name == 'q': 
#		break
#	formatted_name = get_formatted_name(f_name,l_name)
#	print(f"\nHello, {formatted_name}!")

# Practice 8-6
def city_country(city,country):
	"""Display the country information about a city."""
	print(f"{city.title()}, {country.title()}")

city_country('shanghai', 'China')
city_country('new york','united States')
city_country('santiago','chile')

# Practice 8-7
def make_album(artist, title):
	"""Return a dictionary of information about albums."""
	albums = {'artist':artist.title(),'title':title.title()}
	return albums
music_info = make_album('metallica','riding the lightning')
print(music_info)	


def make_album(artist, title, number_of_songs = None):
	"""Return a dictionary of information about albums."""
	albums = {'artist':artist.title(),'title':title.title()}
	if number_of_songs:
		albums['number_of_songs'] = number_of_songs
	return albums
music_info = make_album('metallica','riding the lightning',17)
print(music_info)

#>>>def make_album(artist,title,tracks=0):
#...     """Return a dictionary of information about an album."""
#...     album_dict = {'Artist':artist.title(),'Title':title.title()}
#...     if tracks:
#...             album_dict['tracks']=tracks
#...     return album_dict
#... 
#>>> while True:
#...     print("\nPlease tell me artist name:")
#...     print("(enter 'q' at any time to quit)")
#...     a_name = input("Artist's name:")
#...     if a_name == 'q':
#...             break
#...     t_name = input("Title's name:")
#...     if t_name == 'q':
#...             break
#...     n_track = input("How many songs are in this album:")
#...     if n_track == 'q':
#...             break
#...     album = make_album(a_name, t_name, n_track)
#...     print(album)
#... 

#Please tell me artist name:
#(enter 'q' at any time to quit)
#Artist's name:Mozart
#Title's name:the best of mozart
#How many songs are in this album:13
#{'Artist': 'Mozart', 'Title': 'The Best Of Mozart', 'tracks': '13'}

#Please tell me artist name:
#(enter 'q' at any time to quit)
#Artist's name:q
#>>> 

# Passing a list to a function
def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		print(f"Hello, {name.title()}!")
names = ['hannah','ty','margot']
greet_users(names)

# Modifying a list in a function
def print_models(unprinted_designs,completed_models):
	"""Move each unprinted design to completed models after printing."""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)	
def show_completed_models(completed_models):
	"""Display all models that were printed."""
	print("The following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
unprinted_designs =['phone case','robot pendant','dodecahedron']
completed_models= []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)	
print(unprinted_designs)

#Pratice 8-9
def show_message(messages):
	""" Display each message."""
	for message in messages:
		print(message)
messages = ['Hello, Vivian.','Chapter 7 and 8 in Python Crash Course are two important chapters.','You will finish it soon.']		
show_message(messages)

#Practice 8-10
def show_message(messages):
	""" Display each message."""
	print("\nShowing all messages:")
	for message in messages:
		print(message)
def send_messages(messages,sent_messages):
	"""Move messages to new location."""
	print(f"\nMessage sent: ")
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)

messages = ['Hello, Vivian.','Chapter 7 and 8 in Python Crash Course are two important chapters.','You will finish it soon.']		
show_message(messages)

sent_messages = []
send_messages(messages,sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)


#Practice 8-11
def send_messages(messages):
	"""Display the message that was sent."""
	for message in messages:
		print(f"\nThis message was sent: {message}.")
def show_sent_message(messages,send_messages):
	"""Show the meassage sent to new list."""
	print("\nThe following messages were sent:")
	while messages:
		send_message = messages.pop()
		print(send_message)
		send_messages.append(send_message)


messages = ['Hello, Vivian.','Chapter 7 and 8 in Python Crash Course are two important chapters.','You will finish it soon.']		
send_messages(messages)

send_messages=[]
show_sent_message(messages[:],send_messages)


print(messages)
print(send_messages)














































































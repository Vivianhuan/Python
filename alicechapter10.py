###Chapter 10
# 1. Handling the FileNotFoundError Exception
#filename = 'alice.txt'
#with open(filename, encoding = 'urf-8') as file_object:
#
#output: FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
filename = 'alice.txt'
try:
	with open(filename, encoding = 'utf-8') as file_object:
		contents = file_object.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")

# 2. Analyzing Text
filename = 'alice.txt'

try: 
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
else:
	words = contents.split()
	number_words = len(words)
	print(f"The file {filename} has about {number_words} words.")

# 3. Working with Multiple Files
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		words = contents.split()
		number_words = len(words)
		print(f"The file {filename} has about {number_words} words.")
filename = 'alice.txt'
count_words(filename)	

filenames = ['alice.txt','siddhartha.txt','little_women.txt']
for filename in filenames:
	count_words(filename)	

# 4. Failing Silently: . Python has a pass statement that tells it to do nothing in a block
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		pass
	else:
		words = contents.split()
		number_words = len(words)
		print(f"The file {filename} has about {number_words} words.")

filenames = ['alice.txt','siddhartha.txt','little_women.txt']
for filename in filenames:
	count_words(filename)	

# Practice 10-6 & 10-7
#print("Give me two numbers, and I will add them up.")
#print("Enter 'q' to quit.")
#while True
#	try:
#		first_number = input("First number:")
#		if first_number == 'q':
#			break
#		second_number = input("Second number:")
#		if second_number == 'q':
#			break
#		answer = int(first_number) + int(second_number)
#		print(answer)	
#	except ValueError:
#		print("Sorry, please enter a number.")

# Practice 10-8
def show_names (filename):
	"""Display all names in a file."""
	try: 
		with open(filename, encoding='utf-8') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} is missing.")
	else:
		print(contents.rstrip())
filename = 'cats.txt'
show_names(filename)				

filenames = ['cats.txt','dogs.txt']
for filename in filenames:
	show_names(filename)

# Practice 10-10
filename = 'alice.txt'
with open(filename) as file_object:
	contents = file_object.read()
	num_the = contents.count('the')
	print(num_the)

filename = 'alice.txt'
with open(filename) as file_object:
	contents = file_object.read()
	num_the = contents.lower().count('the')
	print(num_the)

	
























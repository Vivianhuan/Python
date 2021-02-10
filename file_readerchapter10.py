# Reading from a File
######### 1. reading an entire file which is stored in the directory 
#where the file that's currently being  executed (that is, your .py 
#program file) is stored.
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents)	
print(contents.rstrip())
#The 2nd print is to remove the eatra blank line at the end of the output.

#File Paths
# Sometimes the file you want to open won’t be in the same 
#directory as your program file. 
with open('text_files/shoppinglist.txt') as file_object:
	contents = file_object.read()
print(contents)

#You can also tell Python exactly where the file is on your 
#computer regardless of where the program that’s being executed 
#is stored. 
# abosolute file path
file_path = '/Users/Vivian/Desktop/pythonreadsfile/placestovisit.txt'
with open(file_path) as file_object:
	contents = file_object.read()
print(contents)	

######### 2. Reading Line by Line: You can use a for loop on the file 
#object to examine each line from a file one at a time.

with open ('pi_digits.txt') as file_object:
	for line in file_object:
		print(line)


with open ('pi_digits.txt') as file_object:
	for line in file_object:
		print(line.rstrip())
######### 3.  Making a List of Lines from a File
filename = 'text_files/shoppinglist.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())


######### 4. Working with a File's Contents
with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
	
print(pi_string)
print(len(pi_string))

with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()	
print(pi_string)
print(len(pi_string))

######### 5. Large Files: One Million Digits
with open('text_files/pi_million_digits.txt') as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()	
print(f"{pi_string[:52]}...")
print(len(pi_string))	

######### 6. Is Your Birthday Contained in Pi?
with open('text_files/pi_million_digits') as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else: 
	print("Your birthday does not appear in the first million digits of pi.")	

# you can try the above codes in Terminal, because Sublime doesn't have the prompt function.	



















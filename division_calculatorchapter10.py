#Chapter 10 Exceptions
#Exceptions are handled with try-except blocks. A try-except #block asks Python to do something, but it also tells Python what #to do if an exception is raised. When you use try-except blocks, #your programs will continue running even if things start to go #wrong. Instead of tracebacks, which can be confusing for users #to read, users will see friendly error messages that you write.

# 1. Handling the ZeroDivisionError Exception
# print(5/0) -> ZeroDivisionError: division by zero
try: 
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

# 2. Using Exceptions to Prevent Crashes
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")

while True: 
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break
	second_number = input("\nSecond number:")
	if second_number == 'q':	
		break
	answer = int(first_number)/int(second_number)
	print(answer)

###run on Terminal: 
###output: First number:12
#Second number:3
#4.0
#First number:3
#Second number:0
#Traceback (most recent call last):
# File "<stdin>", line 8, in <module>
#ZeroDivisionError: division by zero

#It’s bad that the program crashed, but it’s also not a good idea to 
#let users see tracebacks.

# 3. The else Block
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")

while True: 
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break
	second_number = input("\nSecond number:")
	if second_number == 'q':	
		break
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)			




























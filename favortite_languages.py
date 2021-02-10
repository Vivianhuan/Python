favorite_language = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}
language = favorite_language['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Using get() to access values
alien_0 = {'color':'green','speed':'slow'}
# print(alien_0['points']) you can try to print this code. Doesn't work

alien_0 = {'color':'green','speed':'slow'}
point_value = alien_0.get('points','No point value assigned.')
print(point_value)

# Practice 6-1
friend = {
	'first_name':'Zoe',
	'last_name':'Pan',
	'age': 30,
	'city':'Shanghai'
}
print(friend['first_name'])
print(friend['last_name'])
print(friend['age'])
print(friend['city'])

# Practice 6-2
favorite_number = {
	'vivian': 7,
	'zoe': 5,
	'alice': 3,
	'tom': 1,
	'jack': 10
}
num = favorite_number['vivian']
print(f"Vivian's favorite number is {num}.")

# or by looping all key-value pairs
favorite_number = {
	'vivian': 7,
	'zoe': 5,
	'alice': 3,
	'tom': 1,
	'jack': 10
}
for name, number in favorite_number.items():
	print(f"{name.title()}'s favorite number is {number}.")


# Nesting
favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
}
for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print(f"{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t {language.title()}")
	else:
		print(f"{name.title()}'s favorite languages is:")
		for language in languages:
			print(f"\t {language.title()}")

















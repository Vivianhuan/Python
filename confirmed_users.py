# Moving items from one list to another
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
	current_users = unconfirmed_users.pop()
	print(f"Verifying user: {current_users.title()}")
	confirmed_users.append(current_users)
print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

# Moving all instances of specific values from a list
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

# Filing a dictionary with user input
# because it involves with prompt, so we use terminal to run the codes.

# Practice 7-8
sandwich_orders = ['club sandwich','tuna sandwich','grilled cheese sandwich','cheesesteak sandwich']
finished_sandwiches = []
while sandwich_orders: 
	finished_sandwich = sandwich_orders.pop()
	print(f"\n Verifying order: {finished_sandwich} ")	
	finished_sandwiches.append(finished_sandwich)
print("\nThe following orders are confirmed: ")	
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)

# Practice 7-9

sandwich_orders = sandwich_orders = ['club sandwich','pastrami','tuna sandwich','grilled cheese sandwich','pastrami','cheesesteak sandwich','pastrami']
finished_sandwiches = []
print("I am sorry that we are run out of pastrami.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print("The updated sandwich orders: ")
for sandwich in sandwich_orders: 
	print(sandwich)

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	finished_sandwiches.append(finished_sandwich)
print("\nThe following sandwiches are finished:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)	

# Practice 7-10
#refer to terminal app	
dream_locations = {}
polling_active = True
while polling_active:
	name = input("What is your name?")
	dream_location = input("If you could visit one place in the world, where would you go?")
	dream_locations[name] = dream_location
	repeat = input("Would you like to let another person respond? (yes/no)")
	if repeat == 'no':
		polling_active = False
	for name,dream_location in dream_locations.items():
		print(f"{name} would like to go to {response} for vacation.")

 











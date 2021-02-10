# Sorting a list permanently with the sort() 
cars = ["bmw","audi","toyota","subaru"]
cars.sort()
print(cars)

# Sorting a list permanently in reverse alphabetical order
cars = ["bmw","audi","toyota","subaru"]
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with the sorted()
cars = ["bmw","audi","toyota","subaru"]
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
# Pay attention to the error I made
#print(cars.sorted())
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a list in reverse order (Permanently but can simply reverse back)
cars = ["bmw","audi","toyota","subaru"]
print(f"\n{cars}")

cars.reverse()
print(cars)

# Finding the length of a list in Terminal
# cars = ["bmw","audi","toyota","subaru"]
# len(cars)


# If statement
cars = ["audi","bmw","subaru","toyota"]
for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())



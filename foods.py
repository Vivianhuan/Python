# Copy a list by [ : ]
my_foods = ["pizza","faladel","carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")
print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Practices

my_foods = ["pizza","faladel","carrot cake","ramen","dumplings"]
print("\nThe first three items in the last are:")
print(my_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[1:4])


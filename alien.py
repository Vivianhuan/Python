# Dictinaries with key-value pairs
alien_0 = {"color":"green","points":5}
print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print(f"You just earned {new_points} points.")

# Adding new key-value pairs to the dictinary
# to add a new key-value pair, you would give the name of the dictionary 
# followed by the new key in square brackets along with the new value
alien_0 = {"color":"green","points":5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Starting with an empty dictionary
alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

# Modifying values in a dictinary
# To modify a value in a dictionary, give the name of the dictionary with the
# key in square brackets and then the new value you want associated with that key
# 注意⚠️必须使用单引号去赋予dictionary的value要不然无法run代码
alien_0 = {'color':'green','points':5}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

# Really Good Good Good Example:
alien_0 = {'x_position': 0,'y_position': 25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")
# #Move the alien to the right.
# #Determine how far to move the alien based on its current speed. 
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}.")

alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}.")

# Removing key-value pairs permanently by del statement
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)








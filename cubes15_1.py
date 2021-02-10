 # A number raised to the third power is a cube. Plot the first five
# cubic numbers, and then plot the first 5000 cubic numbers.

import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values, c = y_values, cmap = plt.cm.Reds, s=100)

# Set the title and axes label.
ax.set_title("Cubes Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize =14)
ax.set_ylabel("Cubes of Value", fontsize =14)
ax.tick_params(axis = 'both', which='major', labelsize = 14)

ax.axis([0,6000,0,150000000000])

plt.show()

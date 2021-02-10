from diechapter15 import Die

# Create a D6 (create an instance and call a function back)
die = Die()


# Make some rolls, and store results in a list.
results=[]
for roll_num in range(1000):
	result = die.roll()
	results.append(result)


# Analyzing the results. 
frequencies = []

for value in range(1,die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)	


# Visualize the results
from plotly.graph_objs import Bar, Layout
from plotly import offline

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'Result','dtick':1}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling one D6 1000 times', xaxis=x_axis_config,yaxis=y_axis_config)	
offline.plot({'data':data,'layout':my_layout}, filename = 'd6.html')

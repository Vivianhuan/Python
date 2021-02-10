from diechapter15 import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000000):
	result = die_1.roll() * die_2.roll()
	results.append(result)

frequencies = []
max_result = die_1.num_sides*die_2.num_sides
for value in range(1,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)	

# Visualize the results
from plotly.graph_objs import Bar, Layout
from plotly import offline

x_values = list(range(1, max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'Result','dtick':1}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling two D8 1000000 times', xaxis=x_axis_config,yaxis=y_axis_config)	
offline.plot({'data':data,'layout':my_layout}, filename = 'd6*d6.html')

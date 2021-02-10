import csv
from datetime import datetime

num_rows = 10000

filename = '/Users/Vivian/Desktop/python_work/data/world_fires_1_day.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

####lines = len(list(reader)) to see how many lines in the file.
# In this file, it has more than 27000 lines. 	

	for index,column_header in enumerate(header_row):
		print(index, column_header)	

	# Extracting the information we need to present. 
	
	dates, lons, lats, brightnesses, hover_texts= [],[],[],[],[]
	row_num = 0
	for row in reader:
		current_date = datetime.strptime(row[5],'%Y-%m-%d')
		dates.append(current_date)
		brightness = float(row[2])
		brightnesses.append(brightness)
		lons.append(row[1])
		lats.append(row[0])

		label = f"{current_date.strftime('%Y-%m-%d')}-{brightness}"
		hover_texts.append(label)

		row_num +=1
		if row_num == num_rows:
			break


# Mapping
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'text':hover_texts,
	'marker':{
		'size':[brightness/50 for brightness in brightnesses],
		'color': brightnesses,
		'colorscale':'Reds',
		'reversescale': True,
		'colorbar':{'title': 'brightness'},
	},
}]

my_layout = Layout(
	title = 'World Fires Activity in One Day',
	title_x = 0.5,
	)

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename = 'world_fires_1day.html')




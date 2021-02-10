#The json.load() function converts the data into a format Python can work with
#The json.dump() function takes a JSON data object and a file object, and writes the data to that file
#The indent=4 argument tells dump() to format the data using indentation that matches the data’s structure.

# Pay Attention To:
# The geoJSON format follows the (longitude, latitude) convention, and 
# if you use a different framework it’s important to learn what convention that framework follows.



import json

# Explore the structure of the data. 
filename = '/Users/Vivian/Desktop/python_work/data/eq_data_30_day_m1.json'
with open (filename) as f:
	all_eq_data = json.load(f)

readable_file = '/Users/Vivian/Desktop/python_work/data/readable_eq_data.json'
with open(readable_file,'w') as f:
	json.dump(all_eq_data,f,indent = 4)


all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extracting Magnitudes.Next we will combine all information we need to display.
#mags=[]
#for eq_dict in all_eq_dicts:
#	mag = eq_dict['properties']['mag']
#	mags.append(mag)
#print(mags[:10])

mags, lons, lats, hover_texts  = [],[],[],[]
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	title = eq_dict['properties']['title']
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)
	hover_texts.append(title)
#print(mags[:10])
#print(lons[:5])
#print(lats[:5])

# Building a World Map
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Map the earthquakes. 
data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'text':hover_texts,
	'marker':{
		'size':[3*mag for mag in mags],
		'color': mags,
		'colorscale':'Reds',
		'reversescale': True,
		'colorbar':{'title': 'Magnitude'},
	},
}]

# To see the available colorscales, please refer to show_color_scales.py
my_layout = Layout(
	title = 'Global Earthquakes',
	title_x = 0.5,
	)

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename = 'global_earthquakes.html')



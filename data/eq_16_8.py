import json

# Explore the structure of the data. 
filename = '/Users/Vivian/Desktop/python_work/data/current_eq_30.json'
with open (filename) as f:
	all_eq_data = json.load(f)

currentreadable_file = '/Users/Vivian/Desktop/python_work/data/currentreadable_eq_data.json'
with open(currentreadable_file,'w') as f:
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
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

# Map the earthquakes. 
data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'text':hover_texts,
	'marker':{
		'size':[5*mag for mag in mags],
		'color':mags,
		'colorscale':'Viridis',
		'reversescale': True,
		'colorbar':{'title': 'Magnitude'},
	},
}]

# To see the available colorscales, please refer to show_color_scales.py
my_layout = Layout(title = 'Global Earthquakes in Past 30 Days')

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename = 'global_earthquakes_30.html')






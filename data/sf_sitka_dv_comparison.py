# Missing the weather data for San Francisco. 
import csv
from datetime import datetime


def get_weather_data(filename,dates,highs,lows,date_index,high_index,low_index):
	with open (filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		
		for row in reader:
			current_date = datetime.strptime(row[date_index],'%Y-%m-%d')

			try: 
				high = int(row[high_index])
				low = int(row[low_index])	
			except ValueError:
				print(f"Missing the value of {current_date}")
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)

import matplotlib.pyplot as plt

# Get weather data for Sitka
filename = '/Users/Vivian/Desktop/python_work/data/sitka_weather_2018_simple.csv'
dates, highs, lows = [],[],[]
get_weather_data(filename,dates,highs,lows,date_index=2,high_index=5,low_index=6)

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red', alpha = 0.6)
ax.plot(dates,lows,c='green', alpha = 0.6)
plt.fill_between(dates, highs, lows, facecolor = 'red', alpha = 0.15)

# Get weather data for Death Valley
filename = '/Users/Vivian/Desktop/python_work/data/death_valley_2018_simple.csv'
dates, highs, lows = [],[],[]
get_weather_data(filename,dates,highs,lows,date_index=2,high_index=4,low_index=5)

# Add Death Valley data to current plot. 
ax.plot(dates,highs,c='yellow', alpha = 0.6)
ax.plot(dates,lows,c='blue',alpha = 0.6)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.15)



# Format plot
title = "Daily Rainfall Amounts - 2018\nSitka in AK V.S. Death Valley in CA"
plt.title(title, fontsize = 26)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both',which='major',labelsize = 16)
plt.ylim(10,130)

plt.show()


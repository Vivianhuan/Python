import csv

filename = '/Users/Vivian/Desktop/python_work/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

#The csv module contains a next() function, which returns the next line
#in the file when passed the reader object. 

	for index,column_header in enumerate(header_row):
		print(index,column_header)

# Extracting and Reading Data
# The datetime module
	from datetime import datetime
	# Get dates and high temperatures from this file.
	dates,highs, lows=[],[],[]
	for row in reader:
		current_date = datetime.strptime(row[2],'%Y-%m-%d')
		dates.append(current_date)
		high = int(row[5])
		highs.append(high)
		low = int(row[6])
		lows.append(low)




	
# Plotting Data in a Temperature Chart
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig,ax = plt.subplots()	
ax.plot(dates,highs, c='red',linewidth=1, alpha = 0.5)
ax.plot(dates,lows,c='blue',linewidth=1,alpha = 0.5)
plt.fill_between(dates,highs,lows,facecolor= 'blue', alpha = 0.1)
#The alpha argument at u controls a color’s transparency. 
#An alpha value of 0 is completely transparent, and 1 (the default) is 
#completely opaque.
# fill_between() the list dates for the x-values and then the
# two y-value series highs and lows. The facecolor argument determines 
#the color of the shaded region.



plt.title("Daily high and low temperatures, 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()






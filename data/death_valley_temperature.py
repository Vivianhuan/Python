# In this case We will handle some exceptions (missing values). You can compare
# these codes with sitla_hights.py codes to see the differnece. 

import csv
from datetime import datetime

filename = '/Users/Vivian/Desktop/python_work/data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	for index,column_header in enumerate(header_row):
		print(index,column_header)

	dates,highs,lows=[],[],[]	
	for row in reader:
		current_date = datetime.strptime(row[2],'%Y-%m-%d')
	
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:		
			dates.append(current_date)
			lows.append(low)
			highs.append(high)

import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs, c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

plt.title("Death Valley daily high and low temperatures, 2018",fontsize = 24)	
plt.xlabel('',fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both',which='major',labelsize = 16)

plt.show()	

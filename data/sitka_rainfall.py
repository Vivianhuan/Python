import csv
from datetime import datetime

filename = '/Users/Vivian/Desktop/python_work/data/sitka_weather_2018_simple.csv'
with open (filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	for index, column_header in enumerate(header_row):
		print(index,column_header)

	dates,precipitations = [],[]
	for row in reader:
		current_date = datetime.strptime(row[2],'%Y-%m-%d')

		try: 
			precipitation = float(row[3])
		except ValueError:
			print(f"Missing the value of {current_date}")
		else:
			dates.append(current_date)
			precipitations.append(precipitation)


import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,precipitations,c='green', linewidth=1)

title = "Daily Rainfall Amounts - 2018\nSitka in Alaska"
plt.title(title, fontsize = 26)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize = 16)
plt.tick_params(axis = 'both',which='major',labelsize = 16)

plt.show()


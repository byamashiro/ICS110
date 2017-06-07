import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

import pandas as pd


#=======Neutron monitor Data
nm_data = open('Data/NMDB_OULU_data.txt','r')
#print(nm_data)

data = []

for line in nm_data:
	if '2012-03' in line:
		cleanline = line.strip()
		splitline = cleanline.split(';')
		data.append(splitline)

date_time = [x[0] for x in data]
flux = [y[1] for y in data]


full_data = {'date': date_time, 'value': flux}
df = pd.DataFrame(full_data, columns = ['date', 'value'])
converted_time = pd.to_datetime(df['date'])



#==============Plotting data
#time_format = '%d-%m-%Y %H:%M:%S'
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(converted_time, df.value, 'o', color='blue')
#plt.axvline(x=4481, ymin=0, ymax=1, hold=None, color='purple')
#plt.xlim([tstart, tstop])
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Flux', fontname="Arial", fontsize = 14)
plt.minorticks_on()
#plt.ylim([0,100])
plt.grid(True)
#plt.yscale('log')
#plt.savefig('dopper.pdf', format='pdf', dpi=900)
plt.tight_layout()


ax.xaxis.set_major_formatter(myFmt)

plt.show()



'''
data.split(';')
print(data)
#print(del_data)
'''
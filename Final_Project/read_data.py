import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import csv
import pandas as pd
import sys
import numpy as np


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

#=======Particle Flux
fin0 = open('Data/GOES_proton_flux/g15_epead_p27w_32s_20120306_20120306.csv')
fin1 = open('Data/GOES_proton_flux/g15_epead_p27w_32s_20120307_20120307.csv')
fin2 = open('Data/GOES_proton_flux/g15_epead_p27w_32s_20120308_20120308.csv')
fin3 = open('Data/GOES_proton_flux/g15_epead_p27w_32s_20120309_20120309.csv')
fin4 = open('Data/GOES_proton_flux/g15_epead_p27w_32s_20120310_20120310.csv')
fin5 = open('Data/GOES_proton_flux/g15_epead_p27w_32s_20120311_20120311.csv')
fin6 = open('Data/GOES_proton_flux/g15_epead_p27w_32s_20120312_20120312.csv')


for i in range(284): #284, test is 2915
	fin0.readline()
	fin1.readline()
	fin2.readline()
	fin3.readline()
	fin4.readline()
	fin5.readline()
	fin6.readline()


#header = fin.readlines(283)#[:283] #starstring[:2.isnum()] #readlines puts pointer at end 
#starstring[:4].isnum()
#print(header)

#fin_tot = fin1 + fin2 + fin3
fin_0 = list(csv.reader(fin0))#delimiter=' '
fin_1 = list(csv.reader(fin1))#delimiter=' '
fin_2 = list(csv.reader(fin2))#delimiter=' '
fin_3 = list(csv.reader(fin3))#delimiter=' '
fin_4 = list(csv.reader(fin4))#delimiter=' '
fin_5 = list(csv.reader(fin5))#delimiter=' '
fin_6 = list(csv.reader(fin6))#delimiter=' '


data = fin_0 + fin_1 + fin_2 + fin_3 + fin_4 + fin_5 + fin_6
#proton_date = [a[1] for a in data]

proton_date = []
proton_1 = []
proton_2 = []
proton_3 = []
proton_4 = []

#	if lines and lines[0][:4].isnumeric(): # didnt work because of line 280

for lines in data:
		protondate = lines[0]
		proton1 = lines[6]
		proton2 = lines[9]
		proton3 = lines[12]
		proton4 = lines[15]

		proton_date.append(protondate)
		proton_1.append(proton1)
		proton_2.append(proton2)
		proton_3.append(proton3)
		proton_4.append(proton4)

#date_time = [x[0] for x in data]
#flux = [y[1] for y in data]

proton_data = {'date': proton_date, 'pflux1': proton_1, 'pflux2': proton_2, 'pflux3': proton_3, 'pflux4': proton_4}
df_proton = pd.DataFrame(proton_data, columns = ['date', 'pflux1', 'pflux2', 'pflux3', 'pflux4'])
df_proton.replace('-99999.0', np.nan, inplace=True)
proton_time = pd.to_datetime(df_proton['date'])


#==============Plotting data
#time_format = '%d-%m-%Y %H:%M:%S'
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(converted_time, df.value, '-', color='blue')
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
#plt.clf()


#=========proton flux
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

fig = plt.figure()
ax = fig.add_subplot(111)

#'11.6', '30.6', '63.1', '165'
plt.plot(proton_time, df_proton.pflux1, '-', color='blue')
plt.plot(proton_time, df_proton.pflux2, '-', color='green')
plt.plot(proton_time, df_proton.pflux3, '-', color='orange')
plt.plot(proton_time, df_proton.pflux4, '-', color='red')

#plt.axvline(x=4481, ymin=0, ymax=1, hold=None, color='purple')
#plt.xlim([tstart, tstop])
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Flux', fontname="Arial", fontsize = 14)
plt.minorticks_on()
#plt.ylim([0,100])
plt.grid(True)
plt.yscale('log')
#plt.savefig('dopper.pdf', format='pdf', dpi=900)
plt.tight_layout()

ax.xaxis.set_major_formatter(myFmt)

plt.show()



'''
data.split(';')
print(data)
#print(del_data)
'''
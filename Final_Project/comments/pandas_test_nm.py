import pandas as pd
import requests
import time

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import AutoDateFormatter, AutoDateLocator

import datetime
import numpy as np


import random

import sys

start_date = input('Enter start date (yyyymmdd): ')
start_day = start_date[6:8]
start_month = start_date[4:6]
start_year = start_date[:4]
#start_hour = input('Enter start hour: ')
start_minute = '00'

#start_day = '07'
#start_month = '03'
#start_year = '2012'
#start_hour = '01'
#start_minute = '00'

end_date = input('Enter a end date (yyyymmdd): ')
if end_date == '':
	end_date = start_date

end_day = end_date[6:8]
end_month = end_date[4:6]
end_year = end_date[:4]
#end_hour = input
end_minute = '00'

if len(start_date) != 8 or len(end_date) != 8:
	print('\nDATE ERROR: Dates must have 8 digits.')
	sys.exit(0)

start_hour = input('Enter a start hour or "full": ').zfill(2)
if start_hour.isdigit() == True:
	end_hour = input('Enter a end hour: ').zfill(2)
	if start_date == end_date:
		if (int(end_hour) - int(start_hour)) < 0:
			print('\nTIME ERROR: Difference between two hours must be greater than zero.')
			sys.exit(0)
	elif int(end_hour) > 24 or int(start_hour) > 23:
		print('\nTIME ERROR: Hours must be between 0 and 23.')
		sys.exit(0)

if start_hour.isdigit() == False:
	if start_hour == 'full':
		start_hour = '00'.zfill(2)
		end_hour = '23'.zfill(2)
	else:
		print('\nTIME ERROR: Not a valid alternative hour.')
		sys.exit(0)


#=========NM Stations

list_nm = ['AATB','APTY','ARNM','ATHN','BKSN','CALG','CALM','DOMB',
			'DOMC','DRBS','ESOI','FSMT','HRMS','INVK','IRK2','IRK3',
			'IRKT','JBGO','JUNG','JUNG1','KERG','KIEL','KIEL2','LMKS',
			'MCRL','MGDN','MOSC','MRNY','MWSN','MXCO','NAIN','NANM','NEU3',
			'NEWK','NRLK','NVBK','OULU','PSNM','PTFM','PWNK','ROME','SANB','SNAE'
			,'SOPB','SOPO','TERA','THUL','TIBT','TXBY','YKTK']

num_station = int(input('How many stations to parse: '))
print(f'You are parsing {num_station} station(s)')
#station_multi = input('Enter station names: ')

station_multi = []
for i in range(num_station):
	station = input('Enter station names: ')
	if station == '':
		station = 'OULU'
		station_multi.append(station)
	elif station == 'random':
		station = random.choice(list_nm)
		station_multi.append(station)
	else:
		station_multi.append(station)


#print(f'Neutron Monitor Data from: {station}')
#station = input('Specify NM Station (default-OULU): ')




event_obj_start = datetime.datetime.strptime(f'{start_date} {start_hour}', '%Y%m%d %H')
event_obj_start_str = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H:%M:%S')
event_obj_start_str_date = datetime.datetime.strftime(event_obj_start, '%Y-%m-%d %H')


event_obj_end = datetime.datetime.strptime(f'{end_date} {end_hour}', '%Y%m%d %H')
event_obj_end_str = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H:%M:%S')
event_obj_end_str_date = datetime.datetime.strftime(event_obj_end, '%Y-%m-%d %H')


#list_nm_3 = ['OULU','APTY','INVK']
station_str = ''
for i in station_multi:
	station_str += f'&stations[]={i}'

url = f'http://www.nmdb.eu/nest/draw_graph.php?formchk=1{station_str}&tabchoice=revori&dtype=corr_for_efficiency&tresolution=0&yunits=0&date_choice=bydate&start_day={start_day}&start_month={start_month}&start_year={start_year}&start_hour={start_hour}&start_min={start_minute}&end_day={end_day}&end_month={end_month}&end_year={end_year}&end_hour={end_hour}&end_min={end_minute}&output=ascii'
#url = f'http://www.nmdb.eu/nest/draw_graph.php?formchk=1&stations[]={station}&tabchoice=revori&dtype=corr_for_efficiency&tresolution=0&yunits=0&date_choice=bydate&start_day={start_day}&start_month={start_month}&start_year={start_year}&start_hour={start_hour}&start_min={start_minute}&end_day={end_day}&end_month={end_month}&end_year={end_year}&end_hour={end_hour}&end_min={end_minute}&output=ascii'

#resp = requests.get(url)
nm_data = pd.DataFrame([])

name_list = ['datetime'] + [ str(i) for i in station_multi]

dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
nm_data = pd.read_csv(url, sep=';|\n|\b', skiprows=132, skipfooter=3, engine='python', index_col='datetime', names=name_list, date_parser=dateparse, parse_dates=['datetime']) #, 
#print(nm_data)


#sorter = ['PSNM', 'TIBT', 'ESOI', 'ATHN', 'MXCO', 'ARNM', 'NANM', 'PTFM', 'CALM', 'AATB', 'ROME', 'BKSN', 'HRMS', 'JUNG', 'JUNG1', 'LMKS', 'IRK2', 'IRK3', 'IRKT', 'DRBS', 'NVBK', 'MCRL', 'MOSC', 'NEWK', 'KIEL', 'KIEL2', 'MGDN', 'YKTK', 'KERG', 'CALG', 'OULU', 'SANB', 'SNAE', 'APTY', 'NRLK', 'TXBY', 'FSMT', 'INVK', 'JBGO', 'NAIN', 'PWNK', 'THUL', 'MWSN', 'NEU3', 'SOPB', 'SOPO', 'MRNY', 'DOMB', 'DOMC', 'TERA']
sorter = {'PSNM':0, 'TIBT':1, 'ESOI':2, 'ATHN':3, 'MXCO':4, 'ARNM':5, 'NANM':6, 'PTFM':7, 'CALM':8, 'AATB':9, 'ROME':10, 'BKSN':11, 'HRMS':12, 'JUNG':13, 'JUNG1':14, 'LMKS':15, 'IRK2':16, 'IRK3':17, 'IRKT':18, 'DRBS':19, 'NVBK':20, 'MCRL':21, 'MOSC':22, 'NEWK':23, 'KIEL':24, 'KIEL2':25, 'MGDN':26, 'YKTK':27, 'KERG':28, 'CALG':29, 'OULU':30, 'SANB':31, 'SNAE':32, 'APTY':33, 'NRLK':34, 'TXBY':35, 'FSMT':36, 'INVK':37, 'JBGO':38, 'NAIN':39, 'PWNK':40, 'THUL':41, 'MWSN':42, 'NEU3':43, 'SOPB':44, 'SOPO':45, 'MRNY':46, 'DOMB':47, 'DOMC':48, 'TERA':49}

#nm_data.columns = nm_data.columns.astype("category")
#nm_data.columns.cat.set_categories(sorter, inplace=True)
#df.reindex_axis(sorted(df.columns), axis=1)



#====Plotting
#myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
#xtick_locator = AutoDateLocator()
#xtick_formatter = AutoDateFormatter(xtick_locator)

color_list = ['red','orange','yellow','green','blue','indigo','violet','purple']

for i in station_multi:
	nm_data[f'{i}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color=random.choice(color_list), label= f'{i}')
#nm_data['RCORR_E'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='limegreen', label= 'Corrected for Efficiency')

plt.title(f'Neutron Monitor Data Corrected for Efficiency: {station} Station\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Counts/s', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.grid(True)
#plt.yscale('log')
plt.legend(loc='upper right')
plt.tight_layout()
#ax = fig.add_subplot(111)
ax = plt.gca()

#ax.xaxis.set_major_formatter(myFmt)
#ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
#ax.xaxis.set_major_locator(xtick_locator)
#ax.xaxis.set_major_formatter(xtick_formatter)

plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')


#end_time = time.clock()
#print(f'Elapsed Time: {round(end_time - start_time , 2)} seconds')

#plt.savefig('nm_data.pdf', format='pdf', dpi=900)
plt.show()

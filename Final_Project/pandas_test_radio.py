import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm



#proton_path = 'Data/GOES_proton_flux'

start_date = input('Enter a start date (yyyymmdd): ')
end_date = input('Enter a end date (yyyymmdd): ')

def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )



#===========Define Paths
full_radio_path_start = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/Type3/original/{start_date[0:6]}'
full_radio_path_end = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/Type3/original/{end_date[0:6]}'
full_radio_path = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/Type3/original'



#===========Data
start = datetime.date( year = int(f'{start_date[0:4]}'), month = int(f'{start_date[4:6]}') , day = int(f'{start_date[6:8]}') )
end = datetime.date( year = int(f'{end_date[0:4]}'), month = int(f'{end_date[4:6]}') , day = int(f'{end_date[6:8]}') )

radio_df = pd.DataFrame([])

'''
for date in daterange( start, end ):
	try:
		event_date = str(date).replace('-','')
		print(event_date[0:6])
		print(f'{full_radio_path}/wind{event_date[0:6]}.txt')
		radio_df_ind = pd.read_csv(f'{full_radio_path}/wind{event_date[0:6]}.txt',delim_whitespace=True, comment='#', skiprows=3) #, skipfooter=3) #, header=0)
		#print(radio_df_ind)
		#radio_df = radio_df.append(radio_df_ind)
	except:
		print(f'Missing data for {date}')
		continue
'''
event_date = str(start).replace('-','')
print(event_date[0:6])

#list_header = [str(i) for i in range(258)]
list_header = [str(i) for i in range(12,1041,4)]


print(f'{full_radio_path}/wind{event_date[0:6]}.txt')

dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y %H:%M:%S.%f')


#start_time = time.clock()
#radio_df = pd.read_csv(f'{full_radio_path}/wind{event_date[0:6]}.txt',engine = 'python',delim_whitespace=True ,skiprows=40, names=list_header, skipfooter=3, parse_dates=[['12', '16']], date_parser=dateparse, index_col='12',keep_date_col=True, na_filter = False) #, header=0)
radio_df = pd.read_csv(f'{full_radio_path}/wind{event_date[0:6]}.txt',engine = 'python',delim_whitespace=True ,skiprows=40, names=list_header, skipfooter=3, parse_dates=[['12', '16']], date_parser=dateparse,keep_date_col=True, na_filter = False) #, header=0)

radio_df['avg'] = radio_df.mean(axis=1, numeric_only=True)
#radio_df.loc[radio_df['avg'] <= 0.0] = np.nan #11.6 MeV
#end_time = time.clock()

#print(end_time - start_time)

#sys.exit(0)
#radio_df['avg'].loc[start.strftime('%d-%m-%Y'):end.strftime('%d-%m-%Y')] #gold line

#print(radio_df_ind)
#radio_df = radio_df.append(radio_df_ind)
#print(radio_df)
#print(radio_df)


#radio_time = pd.to_datetime(radio_df['0'] + ' ' + radio_df['1'], dayfirst=True) #xray_time = xray_df[['time_tag']]
#radio_average = radio_df.mean(axis=1, numeric_only=True)
#result = pd.concat([radio_time, radio_average], axis=1, ignore_index=True)
#=========xray flux
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

''' un comment when done testing
fig = plt.figure()
ax = fig.add_subplot(111)
'''


#========reshaping z
#z = list(radio_df.loc[0].loc['20':'1040'])
#z = z.reshape((len(x), len(y)))
#=========end reshaping z

#plt.plot(radio_df['12_16'].loc[start.strftime('%d-%m-%Y'):end.strftime('%d-%m-%Y')], radio_df['avg'].loc[start.strftime('%d-%m-%Y'):end.strftime('%d-%m-%Y')], '-', color='blue', label= '11.6 MeV')
#plt.contourf(radio_df.loc[0].loc['12_16'],radio_df.columns.values[3:259] )
'''
plt.title('GOES-15 Proton Flux', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Flux [pfu]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.grid(True)
#plt.yscale('log')
plt.legend(loc='lower right')
#plt.savefig('xray.pdf', format='pdf', dpi=900)
plt.tight_layout()
'''
#ax = fig.gca(projection='3d')
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')

'''
full_day_list = []
for i in range(24):
	one_second_list = []

	for j in range(256):
	#one_day_list.append(radio_df.loc[0].loc['12_16'])
		one_second_list.append(i)

	full_day_list.append(one_second_list)
'''
one_day_list = []
for i in range(256):
	one_day_list.append(1.0)


ax.plot(one_day_list, [float(i) for i in radio_df.columns.values[3:259]] , radio_df.loc[0].loc['20':'1040'])#,
#                       linewidth=2) #, antialiased=False

#surf = ax.plot_surface(one_day_list, [float(i) for i in radio_df.columns.values[3:259]] , radio_df.loc[0].loc['20':'1040'], cmap=cm.coolwarm,
#                      linewidth=10, antialiased=False)
#ax.set_zlim(1.0, 2.0)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

#fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
'''
threedee = plt.figure().gca(projection='3d')
threedee.scatter(one_day_list, radio_df.loc[0].loc['20':'1040'],radio_df.columns.values[3:259])
threedee.set_xlabel('Index')
threedee.set_ylabel('H-L')
threedee.set_zlabel('Close')
#ax.xaxis.set_major_formatter(myFmt)

#ax.xaxis.set_major_formatter(myFmt)

plt.show()
'''
#ax.xaxis.set_major_formatter(myFmt)
#plt.show()
#plt.clf() # dont include
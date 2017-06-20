import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys


def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

''' #this works, but will break for months, need a more elegant solution with datetime module
event_list = []
event_date = input('Enter event date (yyyymmdd): ')
for i in range(4):
	event_time = str(int(event_date) + int(i))
	event_list.append(event_time)

print(event_list)
'''

start_date = input('Enter a start date (yyyymmdd): ')
end_date = input('Enter a end date (yyyymmdd): ')

#year = int(f'{start_date[0:4]}')
#month = int(f'{start_date[4:6]}')
#day = int(f'{start_date[6:8]}')
#print(year, month, day)

#sys.exit(0)

start = datetime.date( year = int(f'{start_date[0:4]}'), month = int(f'{start_date[4:6]}') , day = int(f'{start_date[6:8]}') )
end = datetime.date( year = int(f'{end_date[0:4]}'), month = int(f'{end_date[4:6]}') , day = int(f'{end_date[6:8]}') )

xray_df = pd.DataFrame([])

for date in daterange( start, end ):
	event_date = str(date).replace('-','')
	print(event_date)
	xray_df_ind = pd.read_csv(f'Data/GOES_xray_flux/g15_xrs_2s_{event_date}_{event_date}.csv', skiprows=138, header=0)
	xray_df = xray_df.append(xray_df_ind)

xray_df.loc[xray_df['A_FLUX'] <= 0.0] = np.nan
xray_df.loc[xray_df['B_FLUX'] <= 0.0] = np.nan


'''
	if event_date == start_date:
		xray_df_1 = pd.read_csv(f'Data/GOES_xray_flux/g15_xrs_2s_{event_date}_{event_date}.csv', skiprows=138, header=0)
		xray_df = xray_df.append(xray_df_1)

		print(event_date == start_date)
	else:
'''

	#print(xray_df_2)
	#print(event_date == start_date)

#print(xray_df)
#sys.exit(0)

#sys.exit(0)
''' #this segment of the code works for one file
xray_df = pd.read_csv(f'Data/GOES_xray_flux/g15_xrs_2s_{event_date}_{event_date}.csv', skiprows=138, header=0)
xray_df.replace('-99999.0', np.nan, inplace=True) #replaces bad data with np.nan
xray_df.replace('0.0', np.nan, inplace=True)
'''


xray_time = pd.to_datetime(xray_df['time_tag']) #xray_time = xray_df[['time_tag']]


xray_A_flux = xray_df['A_FLUX']
#xray_A_flux[(xray_A_flux <= 0.0)] = np.nan
#xray_A_flux.loc[xray_A_flux['A_FLUX'] <= 0.0] = np.nan


xray_B_flux = xray_df['B_FLUX']
#xray_B_flux[(xray_B_flux <= 0.0)] = np.nan




#xray_A_flux.replace('-99999.0', np.nan, inplace=True) #replaces bad data with np.nan
#xray_A_flux.replace('0.0', np.nan, inplace=True)
#print(min(xray_A_flux), min(xray_B_flux))

#sys.exit(0)

#xray_data = {'xrdate': xray_date, 'xrflux1': xray_1, 'xrflux2': xray_2}
#df_xray = pd.DataFrame(xray_data, columns = ['xrdate', 'xrflux1', 'xrflux2'])
#df_xray.replace('-99999.0', np.nan, inplace=True) #replaces bad data with np.nan
#df_xray.replace('0.0', np.nan, inplace=True)

#=========xray flux
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

fig = plt.figure()
ax = fig.add_subplot(111)

#'11.6', '30.6', '63.1', '165'
plt.plot(xray_time, xray_A_flux, '-', color='blue')
plt.plot(xray_time, xray_B_flux, '-', color='red')

#plt.axvline(x=4481, ymin=0, ymax=1, hold=None, color='purple')
#plt.xlim([tstart, tstop])
plt.title('GOES-15 Xray Flux', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Flux [Wm$^2$]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
#plt.ylim([0,1])
plt.grid(True)
plt.yscale('log')
#plt.savefig('xray.pdf', format='pdf', dpi=900)
plt.tight_layout()

ax.xaxis.set_major_formatter(myFmt)

plt.show()
#plt.clf()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys



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

list_header = list(range(258))


print(f'{full_radio_path}/wind{event_date[0:6]}.txt')
radio_df = pd.read_csv(f'{full_radio_path}/wind{event_date[0:6]}.txt',delim_whitespace=True ,skiprows=40, names=list_header, skipfooter=3) #, header=0)
#print(radio_df_ind)
#radio_df = radio_df.append(radio_df_ind)
#print(radio_df)



radio_time = pd.to_datetime(radio_df[0] + ' ' + radio_df[1], dayfirst=True) #xray_time = xray_df[['time_tag']]
radio_average = radio_df.mean(axis=1, numeric_only=True)

result = pd.concat([radio_time, radio_average], axis=1, ignore_index=True)

#=========xray flux
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(result[0], result[1], '-', color='blue', label= '11.6 MeV')

plt.title('GOES-15 Proton Flux', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Flux [pfu]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.grid(True)
#plt.yscale('log')
plt.legend(loc='lower right')
#plt.savefig('xray.pdf', format='pdf', dpi=900)
plt.tight_layout()


ax.xaxis.set_major_formatter(myFmt)

plt.show()
#plt.clf()
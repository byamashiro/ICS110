import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import glob



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

for date in daterange( start, end ):
	try:
		event_date = str(date).replace('-','')
		print(event_date[0:6])
		print(f'{full_radio_path}/wind{event_date[0:6]}.txt')
		radio_df_ind = pd.read_csv(f'{full_radio_path}/wind{event_date[0:6]}.txt',delim_whitespace=True, comment='#', header = 0, skiprows=39, skipfooter=3) #, header=0)
		#print(radio_df_ind)
		radio_df = radio_df.append(radio_df_ind)
	except:
		print(f'Missing data for {date}')
		continue

#print(radio_df)

print(radio_df)
sys.exit(0)

radio_time = pd.to_datetime(radio_df[0:1]) #xray_time = xray_df[['time_tag']]
print(radio_time)



radio_df['avg'] = radio_df.mean(axis=1, numeric_only=True)



radio_df.loc[radio_df['P3W_UNCOR_FLUX'] <= 0.0] = np.nan #11.6 MeV
radio_df.loc[radio_df['P4W_UNCOR_FLUX'] <= 0.0] = np.nan #30.6 MeV
radio_df.loc[radio_df['P5W_UNCOR_FLUX'] <= 0.0] = np.nan #63.1 MeV
radio_df.loc[radio_df['P6W_UNCOR_FLUX'] <= 0.0] = np.nan #165 MeV


radio_3W_flux = radio_df['P3W_UNCOR_FLUX']	#11.6 MeV
radio_4W_flux = radio_df['P4W_UNCOR_FLUX']	#30.6 MeV
radio_5W_flux = radio_df['P5W_UNCOR_FLUX']	#63.1 MeV
radio_6W_flux = radio_df['P6W_UNCOR_FLUX']	#165 MeV

#=========xray flux
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(radio_time, radio_3W_flux, '-', color='red', label= '11.6 MeV')
plt.plot(radio_time, radio_4W_flux, '-', color='orange', label = '30.6 MeV')
plt.plot(radio_time, radio_5W_flux, '-', color='green', label= '63.1 MeV')
plt.plot(radio_time, radio_6W_flux, '-', color='blue', label = '165 MeV')

plt.title('GOES-15 Proton Flux', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Flux [pfu]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.grid(True)
plt.yscale('log')
plt.legend(loc='lower right')
#plt.savefig('xray.pdf', format='pdf', dpi=900)
plt.tight_layout()


ax.xaxis.set_major_formatter(myFmt)

plt.show()
#plt.clf()
import pandas as pd



start_day = '01'
start_month = '01'
start_year = '2012'
start_hour = '00'
start_minute = '00'

end_day = '01'
end_month = '05'
end_year = '2012'
end_hour = '00'
end_minute = '00'




url = f"http://www.nmdb.eu/nest/draw_graph.php?formchk=1&stations[]=OULU&tabchoice=revori&dtype=corr_for_efficiency&tresolution=0&yunits=0&date_choice=bydate&start_day={start_day}&start_month={start_month}&start_year={start_year}&start_hour={start_hour}&start_min={start_minute}&end_day={end_day}&end_month={end_month}&end_year={end_year}&end_hour={end_hour}&end_min={end_minute}&output=ascii"


nm_data = pd.read_csv(url, skiprows=200, sep=';', skipfooter=100)

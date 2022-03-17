import csv
from datetime import datetime

from pyparsing import delimited_list

#Create file objects.
open_sitka_file = open("sitka_weather_2018_simple.csv","r")
open_death_valley_file = open("death_valley_2018_simple.csv","r")

#Create a CSV file.
sitka_csv_file = csv.reader(open_sitka_file, delimiter = ",")
dv_csv_file = csv.reader(open_death_valley_file, delimiter = ",")


#Skip the first row of each file.
sitka_header_row = next(sitka_csv_file)
dv_header_row = next(dv_csv_file)



"""
for index, column_header in enumerate(sitka_header_row):
    if column_header == "NAME":
        next(sitka_csv_file)
        next(sitka_csv_file)
        sitka_station_name = sitka_header_row[index]

    print(index, column_header)


for index, column_header in enumerate(dv_header_row):
    if column_header == "TMAX":
        dv_tmax = column_header
    elif column_header == "TMIN":
        dv_tmin = column_header
    elif column_header == "NAME":
        next(dv_csv_file)
        dv_station_name = column_header

"""


#Create variables for the TMAX, TMIN, and DATE indices.
sitka_tmax_index = sitka_header_row.index("TMAX")
sitka_tmin_index = sitka_header_row.index("TMIN")
sitka_date_index = sitka_header_row.index("DATE")
sitka_name_index = sitka_header_row.index("NAME")

dv_tmax_index = dv_header_row.index("TMAX")
dv_tmin_index = dv_header_row.index("TMIN")
dv_date_index = dv_header_row.index("DATE")
#dv_name_index = dv_header_row.index("NAME")


#Create lists for the highs, lows, dates, and station names for sitka and death valley.
sitka_highs = []
sitka_lows = []

dv_highs = []
dv_lows = []

sitka_dates = []
dv_dates = []

#sitka_station_name = []
#dv_station_name = []



#Extract all the high and low temps from the sitka file and add them to the list.
for row in sitka_csv_file:
    sitka_highs.append(int(row[sitka_tmax_index]))
    sitka_lows.append(int(row[sitka_tmin_index]))
    current_date = datetime.strptime(row[sitka_date_index], "%Y-%m-%d")
    sitka_dates.append(current_date)
    #sitka_station_name.append(str(row[sitka_name_index]))


#Extract all the high and low temps from the death_valley file and add them to the list.
for row in dv_csv_file:

    try:
        current_date = datetime.strptime(row[dv_date_index], "%Y-%m-%d")
        high = int(row[dv_tmax_index])
        low = int(row[dv_tmin_index])
        
    except ValueError:
        print(f"Missing data for {current_date}")  

    else:    
        dv_highs.append(high)
        dv_lows.append(low)
        dv_dates.append(current_date)




import matplotlib.pyplot as plt

#Create the sitka subplot.
plt.subplot(2, 1, 1)
plt.plot(sitka_dates, sitka_highs, c = "red")
plt.plot(sitka_dates, sitka_lows, c = "blue")
plt.title("SITKA AIRPORT, AK US")
#plt.title(sitka_station_name)
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor = "blue", alpha = 0.1)

#Create the death valley subplot.
plt.subplot(2, 1, 2)
plt.plot(dv_dates, dv_highs, c = "red")
plt.plot(dv_dates, dv_lows, c = "blue")
plt.title("DEATH VALLEY, CA US")
#plt.title(dv_station_name)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor = "blue", alpha = 0.1)


#Display the suptitle.
plt.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")
#plt.suptitle(f"Temperature comparison between {sitka_station_name} and {dv_station_name}")

plt.show()
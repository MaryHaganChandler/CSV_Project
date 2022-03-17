import csv
from datetime import datetime

from pyparsing import delimited_list

#Create a file object.
open_sitka_file = open("sitka_weather_2018_simple.csv","r")
open_death_valley_file = open("death_valley_2018_simple.csv","r")

#Create a CSV file.
sitka_csv_file = csv.reader(open_sitka_file, delimiter = ",")
dv_csv_file = csv.reader(open_death_valley_file, delimiter = ",")


#Skip the first row.
sitka_header_row = next(sitka_csv_file)
dv_header_row = next(dv_csv_file)



for index, column_header in enumerate(sitka_header_row):
    if column_header == "TMAX":
        sitka_tmax = column_header
    elif column_header == "TMIN":
        sitka_tmin = column_header
    elif column_header == "STATION":
        sitka_station = column_header


for index, column_header in enumerate(dv_header_row):
    if column_header == "TMAX":
        dv_tmax = column_header
    elif column_header == "TMIN":
        dv_tmin = column_header
    elif column_header == "STATION":
        dv_station = column_header



sitka_highs = []
sitka_lows = []
dv_highs = []
dv_lows = []
sitka_dates = []
dv_dates = []



#Extract all the high and low temps from the sitka file and add them to the list.
for row in sitka_csv_file:
    sitka_highs.append(int(row[5]))
    sitka_lows.append(int(row[6]))
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    sitka_dates.append(current_date)

#Extract all the high and low temps from the death_valley file and add them to the list.
for row in dv_csv_file:

    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
        
    except ValueError:
        print(f"Missing data for {current_date}")  
            #This is a new way to print something out where you don't need
            #   to have more quotes and commas, and you can use quotes inside
            #   it. You put any variables in curly brackets.

    else:    
        dv_highs.append(high)
        dv_lows.append(low)
        dv_dates.append(current_date)




import matplotlib.pyplot as plt #pyplot is usually referred to as plt

fig = plt.figure()      #Created this so we can format the date better


"""
plt.plot(dates, highs, c = "red")
plt.plot(dates, lows, c = "blue")

plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1)
    #Give this function one x and two y's
    #Alpha is the transparency; alpha ranges from 1 to 0, where 0 is
    #   the most transparent and 1 is not transparent

plt.title("Daily high and low temperatures - 2018",fontsize = 16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)",fontsize=16)

plt.tick_params(axis = "both",which="major",labelsize=16)
    #Tick paramaters are the ticks that are on the graph, we want to show
    #   them on both the x and y axis, and we want to show the major tick
    #   marks.

fig.autofmt_xdate()     #Makes the dates slanted so we can see the whole thing

#plt.show()

"""


plt.subplot(2, 1, 1)
    #We give this three arguments: number of rows we want, number of columns
    #   we want, and which subplot we want to make (the first, second, etc.)
plt.plot(sitka_dates, sitka_highs, c = "red")
plt.plot(sitka_dates, sitka_lows, c = "blue")
plt.title(sitka_station)
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor = "blue", alpha = 0.1)
    #Give this function one x and two y's
    #Alpha is the transparency; alpha ranges from 1 to 0, where 0 is
    #   the most transparent and 1 is not transparent

plt.subplot(2, 1, 2)
plt.plot(dv_dates, dv_highs, c = "red")
plt.plot(dv_dates, dv_lows, c = "blue")
plt.title(dv_station)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor = "blue", alpha = 0.1)
    #Give this function one x and two y's
    #Alpha is the transparency; alpha ranges from 1 to 0, where 0 is
    #   the most transparent and 1 is not transparent

plt.suptitle(f"Temperature comparison between {sitka_station} and {dv_station}")

plt.show()
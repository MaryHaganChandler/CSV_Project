# Copied sitka_2 to start sitka_3

#Objectives for sitka_3
# 1) Changing the file to include all the data for the year of 2018
# 2) Changing the title to Daily high and low temperatures - 2018
# 3) Extracting the low temperatures from the file and adding to the chart
# 4) Shading in the area between high and low



import csv
from datetime import datetime

#Create a file object.
open_file = open("death_valley_2018_simple.csv","r")

#Create a CSV file.
csv_file = csv.reader(open_file, delimiter = ",")

#Skip the first row.
header_row = next(csv_file)
print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)



highs = []
lows = []
dates = []

#Extract all the max temperatures from the file and add them to the list.
for row in csv_file:

    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
        
    except ValueError:
        print(f"Missing data for {current_date}")

    else:    
        highs.append(high)
        lows.append(low)
        dates.append(current_date)      #Can do this line and above in one line

#Print out the lists.
print(highs)
print(dates)




import matplotlib.pyplot as plt #pyplot is usually referred to as plt

fig = plt.figure()      #Created this so we can format the date better

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

plt.show()




























"""

#Supposed to copy and paste from sitka_3, but Mary typed it out

import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print(header_row)


for index, column_header in enumerate(header_row):
    print(index, column_header)


highs = []
dates = []
lows = []

for row in csv_file:

    try:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])

    except ValueError:
        print(f"Missing data for {current_date}")   #This is a new way to print something
                #out where you don't need to have more quotes and commas, and you can use
                #quotes inside it. You put any variables in curly brackets.

    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)


print(highs)
print(lows)

import matplotlib.pyplot as plt

fig = plt.figure()

#More here


"""
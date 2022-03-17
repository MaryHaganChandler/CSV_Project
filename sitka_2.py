#Copied sitka_1 to start sitka_2
#Using the datetime module
#Adding dates to the x axis for the month of July 2018


import csv
from datetime import datetime

#Create a file object.
open_file = open("sitka_weather_07-2018_simple.csv","r")

#Create a CSV file.
csv_file = csv.reader(open_file, delimiter = ",")

#Skip the first row.
header_row = next(csv_file)


for index, column_header in enumerate(header_row):
    print(index, column_header)


highs = []
dates = []

#EXAMPLE of how datetime works -- irrelevant
#test_date = datetime.strptime("2018-01-01", "%Y-%m-%d")
#print(test_date)



#Extract all the max temperatures from the file and add them to the list.
for row in csv_file:
    highs.append(int(row[5]))
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(current_date)      #Can do this line and above in one line

#Print out the lists.
print(highs)
print(dates)




import matplotlib.pyplot as plt #pyplot is usually referred to as plt

fig = plt.figure()      #Created this so we can format the date better

plt.plot(dates, highs, c = "red")

plt.title("Daily high temperatures, July 2018",fontsize = 16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)",fontsize=16)

plt.tick_params(axis = "both",which="major",labelsize=16)
    #Tick paramaters are the ticks that are on the graph, we want to show
    #   them on both the x and y axis, and we want to show the major tick
    #   marks.

fig.autofmt_xdate()     #Makes the dates slanted so we can see the whole thing

plt.show()
#Import CSV module
import csv

#Create a file object.
open_file = open("sitka_weather_07-2018_simple.csv","r")

#Create a CSV file.
csv_file = csv.reader(open_file, delimiter = ",")

#Skip the first row.
header_row = next(csv_file)

#Determine what type the header row is.
#print(type(header_row)) #Every row in this file will be a list.

for index, column_header in enumerate(header_row):
    #Enumerate() is a function in Python that will give us the index
    #   location and the element in that location, so you have a
    #   description of what your list looks like.
    #You can use enumerate on any kind of list object.
    print(index, column_header)


#Create an empty list.
highs = []

#Extract all the max temperatures from the file and add them to the list.
for row in csv_file:
    highs.append(int(row[5]))

#Print out the list.
print(highs)

import matplotlib.pyplot as plt #pyplot is usually referred to as plt

plt.plot(highs, c = "red")

plt.title("Daily high temperatures, July 2018",fontsize = 16)
plt.xlabel("")
plt.ylabel("Temperatures (F)",fontsize=16)

plt.tick_params(axis = "both",which="major",labelsize=16)
    #Tick paramaters are the ticks that are on the graph, we want to show
    #   them on both the x and y axis, and we want to show the major tick
    #   marks.
plt.show()
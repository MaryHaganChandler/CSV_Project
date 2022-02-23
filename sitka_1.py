#Create a file object, create csv object, skip header file

import csv

open_file = open("sitka_weather_07-2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)
print(type(header_row))

for index, column_header in enumerate(header_row):
        #You can use enumerate on any kind of list object.
    print(index, column_header)

#Create an empty list, extract highs (max temps) and add them to the list, and then print out the list

highs = []

for row in csv_file:
    highs.append(int(row[5]))

print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c = "red")

plt.title("Daily high termperatures, July 2018",fontsize = 16)
plt.xlabel("")
plt.ylabel("Termperatures {F}",fontsize=16)

plt.tick_params(axis = "both",which="major",labelsize=16)

plt.show()
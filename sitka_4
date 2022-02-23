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


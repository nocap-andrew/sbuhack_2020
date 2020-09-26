import csv
import json

with open("C:/Users/andre/Desktop/SBUHack/data/NYPD_crime_data.csv") as csv_file:
    lat_list = []
    long_list = []
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if (row[-2] != '' and row[-3] != '' and line_count < 1000):
                line_count += 1
                temp = float(row[-3])
                lat_list.append(temp)
                temp = float(row[-2])
                long_list.append(temp)

    with open("C:/Users/andre/Desktop/SBUHack/data/latitudes.json", "w") as f:
        json.dump(lat_list, f)
    with open("C:/Users/andre/Desktop/SBUHack/data/longtitudes.json", "w") as f1:
        json.dump(long_list, f1)
    print(f'Processed {line_count} lines.')


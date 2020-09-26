import os
import json
import googlemaps

gmaps = googlemaps.Client(key=os.getenv('GOOGLE_API_KEY'))


def read_csv():
    modzcta = {}
    with open('data_by_modzcta.csv', 'r') as data:
        data.readline().split(',')
        lines = data.readlines()
        for line in lines:
            data = dict()
            location = dict()

            line = line.strip().split(",")

            geocode_result = gmaps.geocode(str(line[0]))

            data["COVID_CASE_COUNT"], data["COVID_CASE_RATE"], data["COVID_DEATH_COUNT"], data["COVID_DEATH_RATE"], data["PERCENT_POSITIVE"], data["TOTAL_COVID_TESTS"] = int(line[3]), float(line[4]), int(line[6]), float(line[7]), float(line[8]), int(line[9])
            location["LAT"], location["LNG"]= geocode_result[0]['geometry']["location"]["lat"],  geocode_result[0]['geometry']["location"]["lng"]
            data["LOCATION"] = location
            modzcta[line[1]] = data

    with open('parse_covid_data.json', 'w') as outfile:
        json.dump(modzcta, outfile)


if __name__ == "__main__":
    read_csv()
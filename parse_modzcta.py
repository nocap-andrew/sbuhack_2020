import os
import json
import googlemaps

gmaps = googlemaps.Client(key=os.getenv('GOOGLE_API_KEY'))


def read_csv_modzcta():
    modzcta = {}
    with open('dataset/data_by_modzcta.csv', 'r') as data:
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

    with open('dataset/parse_covid_data.json', 'w') as outfile:
        json.dump(modzcta, outfile)
        outfile.close()


def read_parse_covid_data():
    lat = []
    lng = []
    with open('dataset/parse_covid_data.json', 'r') as json_file:
        data = json.load(json_file)
        for key in data:
            lng.append(data[key]["LOCATION"]["LNG"])
            lat.append(data[key]["LOCATION"]["LAT"])
        json_file.close()
    with open('dataset/latitude.txt', 'w') as f:
        for l in lat:
            f.write("%s\n" % l)
        f.close()
    with open('dataset/longitude.txt', 'w') as f:
        for l in lng:
            f.write("%s\n" % l)
        f.close()


if __name__ == "__main__":
    # read_csv_modzcta()
    read_parse_covid_data()

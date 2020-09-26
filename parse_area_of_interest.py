import simplejson
import json

def read_parse_attractions():
    lat = list()
    lng = list()
    attractions = dict()
    with open('dataset/area_of_interest/Areas_of_Interest_Centroids.csv', 'r') as data:
        data.readline().split(',')
        lines = data.readlines()
        for line in lines:
            n = line.split(',')
            name = n[3]
            line = line.split()
            location = dict()
            location['LNG'] = float(line[1].strip('()'))
            lng.append(float(line[1].strip('()')))

            location['LAT'] = float(line[2].split(',')[0].strip('()'))

            lat.append(float(line[2].split(',')[0].strip('()')))
            attractions[name] = location

    with open('dataset/area_of_interest/attractions_lat.txt', 'w') as f:
        simplejson.dump(lat, f)
        f.close()
    with open('dataset/area_of_interest/attractions_lng.txt', 'w') as f:
        simplejson.dump(lng, f)
        f.close()
    with open('dataset/area_of_interest/attractions.json', 'w') as f:
        json.dump(attractions, f)
        f.close()

if __name__ == "__main__":
    read_parse_attractions()

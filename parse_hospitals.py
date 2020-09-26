import simplejson


def read_parse_hospital():
    lat = list()
    lng = list()
    boroughs = ['BROOKLYN', 'QUEENS', 'MANHATTAN', 'BRONX', 'STATEN ISLAND']
    with open('dataset/Hospitals.csv', 'r') as data:
        data.readline().split(',')
        lines = data.readlines()
        for line in lines:
            line = line.strip().split(",")
            if line[6] in boroughs and line[12] == 'OPEN':
                lat.append(float(line[17]))
                lng.append(float(line[18]))
    with open('dataset/hospital_latitude.txt', 'w') as f:
        simplejson.dump(lat, f)
        f.close()
    with open('dataset/hospital_longitude.txt', 'w') as f:
        simplejson.dump(lng, f)
        f.close()


if __name__ == "__main__":
    read_parse_hospital()

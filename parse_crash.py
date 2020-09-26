import simplejson


def read_parse_crash():
    lat = list()
    lng = list()
    with open('dataset/crashes/Motor_Vehicle_Collisions_-_Crashes.csv', 'r') as data:
        data.readline().split(',')
        lines = data.readlines()
        for line in lines:
            line = line.strip().split(",")
            if line[0][0] == "1" or line[0][0] == "0":
                if line[0].split('/')[2] == "2020" and line[4] != "":
                    lat.append(float(line[4]))
                    lng.append(float(line[5]))

    with open('dataset/crashes/crashes_latitude.txt', 'w') as f:
        simplejson.dump(lat, f)
        f.close()
    with open('dataset/crashes/crashes_longitude.txt', 'w') as f:
        simplejson.dump(lng, f)
        f.close()


if __name__ == "__main__":
    read_parse_crash()

import simplejson


def read_parse_shooting():
    lat = list()
    lng = list()
    with open('dataset/shootings/NYPD_Shooting_Incident_Data__Year_To_Date_.csv', 'r') as data:
        data.readline().split(',')
        lines = data.readlines()
        for line in lines:
            line = line.strip().split(",")
            if line[1][0] == "1" or line[1][0] == "0":
                if line[1].split('/')[2] == "2020" and line[16] != "":
                    lat.append(float(line[16]))
                    lng.append(float(line[17]))

    with open('dataset/shootings/shootings_latitude.txt', 'w') as f:
        simplejson.dump(lat, f)
        f.close()
    with open('dataset/shootings/shootings_longitude.txt', 'w') as f:
        simplejson.dump(lng, f)
        f.close()


if __name__ == "__main__":
    read_parse_shooting()

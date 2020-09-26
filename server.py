from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)


@app.route('/', methods = ["GET"])

def main():
    with open("C:/Users/andre/Desktop/SBUHack/data/latitudes.json", 'r') as json_file:
        latitudes = json.load(json_file)
    with open("C:/Users/andre/Desktop/SBUHack/data/longtitudes.json", 'r') as json_file:
        longtitudes = json.load(json_file)

    return render_template("index.html")

@app.route('/address', methods = ["POST"])

def handle_address():
    user_address = request.form['address']
    crime_toggle = request.form['crime_toggle']
    covid_toggle = request.form['covid_toggle']
    hospital_toggle = request.form['hospital_toggle']
    print(user_address, crime_toggle, covid_toggle, hospital_toggle)



if __name__ == "__main__":
    app.run(debug = True)
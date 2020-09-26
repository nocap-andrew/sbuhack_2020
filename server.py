from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)


@app.route('/', methods = ["GET"])

def main():
    crimes = {}
    with open("./data/latitudes.json", 'r') as json_file:
        crimes["latitudes"] = json.load(json_file)
    with open("./data/longtitudes.json", 'r') as json_file:
        crimes["longtitudes"] = json.load(json_file)

    covid = {}
    with open("./dataset/latitudes.json", 'r') as json_file:
        covid["latitudes"] = json.load(json_file)
    with open("./dataset/longtitudes.json", 'r') as json_file:
        covid["longtitudes"] = json.load(json_file)

    return render_template("index.html", crimes = crimes, covid = covid)



if __name__ == "__main__":
    app.run(debug = True)

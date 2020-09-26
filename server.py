from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

def import_data(type):
    data = {}
    with open(f"./data/{type}_data/latitudes.json", 'r') as json_file:
        data["latitudes"] = json.load(json_file)
    with open(f"./data/{type}_data/longitudes.json", 'r') as json_file:
        data["longitudes"] = json.load(json_file)
    return

@app.route('/', methods = ["GET"])
def main():
    data = {}

    data["crimes"] = import_data("crimes")
    data["covid"] = import_data("covid")
    data["crushes"] = import_data("crushes")

    return render_template("index.html", data = data)



if __name__ == "__main__":
    app.run(debug = True)

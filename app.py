from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import requests

app = Flask(__name__)
CORS(app)

df = pd.read_csv("data/file.csv")

@app.route("/get_data", methods=["GET"])
def get_data():
    risk_category = request.args.get("Risk_Category", "High")
    filtered_df = df[df['Risk_Category'] == risk_category]
    data = filtered_df[["Lat", "Long", "HOUR", "OCCURRED_ON_DATE", "OFFENSE_DESCRIPTION", "Risk_Category"]].to_dict(orient="records")
    return jsonify(data)

@app.route("/get_route", methods=["GET"])
def get_route():
    start_lat = request.args.get("start_lat")
    start_lng = request.args.get("start_lng")
    end_lat = request.args.get("end_lat")
    end_lng = request.args.get("end_lng")
    api_key = "AIzaSyCiCncgh72xOpcY7e-dcH8BgpDT4oKEgFE"

    directions_url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_lat},{start_lng}&destination={end_lat},{end_lng}&key={api_key}"
    
    response = requests.get(directions_url)
    directions_data = response.json()

    return jsonify(directions_data)

@app.route("/get_crimes_along_route", methods=["POST"])
def get_crimes_along_route():
    points = request.json.get("points", [])
    radius = 0.001  # Approx. distance in degrees (small radius for nearby crimes)

    nearby_crimes = []
    for point in points:
        lat, lng = point["lat"], point["lng"]
        filtered_df = df[
            (df["Lat"].between(lat - radius, lat + radius)) & 
            (df["Long"].between(lng - radius, lng + radius))
        ]
        crimes = filtered_df[["Lat", "Long", "HOUR", "OCCURRED_ON_DATE", "OFFENSE_DESCRIPTION", "Risk_Category"]].to_dict(orient="records")
        nearby_crimes.extend(crimes)

    return jsonify(nearby_crimes)

if __name__ == "__main__":
    app.run(debug=True)

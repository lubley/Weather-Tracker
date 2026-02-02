from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
 

@app.route("/", methods=["GET"])
def home():
    city = request.args.get("city")
    weather = None
    error = None

    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        #for debugging.
        print(f"City: {city}, Status: {response.status_code}, Response: {response.text}")

        if response.status_code == 200:
            data = response.json()
            weather = {
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"].title()
            }
        else:
            error = f"Could not fetch weather for '{city}'. Please check the city name."
            #prints error if incorrect city name

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)

